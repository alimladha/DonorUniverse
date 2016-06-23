import os
import numpy as np
import sequence
from sequence import Node, sequenceObject
import csv
from profile import Donor
import Queue, sets
from UniverseGUI import raiseFileError

taxonomicMap = [] ##global taxonomic Map 
donors=[] ##global list of donors
sdiAverage = 0
jsdAverage = 0
fprowAverage = 0
totalSCFAAverage = 0

def loadSequenceData():
    '''
    This function loads the sequence data from OTUtable.txt, it puts the data into sequenceObjects with
    internal Nodes. It grabs all information regardless of whether the donor exists in the donorList.csv
    '''
    #load OTU data as table
    table= np.genfromtxt('OTUtable.txt', dtype = None, skip_header=1)
    
    #loadOTU header
    txt=open('OTUtable.txt')
    header=txt.readline().split()
    
    #for each donor create a sequence object
    sequences = [] # create empty list of sequenceObjects
    for column in xrange(1, len(header)-1):
        ##find the Donor ID
        donorIDsampleID = header[column].split('_') ## [donorID, sampleID]
        donor = donorIDsampleID[0]
        sample = donorIDsampleID[1]
        sixteenS = sequence.sequenceObject() #create sequence object
        sixteenS.donor=int(donor)
        sixteenS.sample=int(sample)
        nameColumn = len(header)-1 #define column where taxonomic data is located
        otuColumn = 0 #define column where OTU ID is located
        for row in table: #iterate through each OTU
            otuValue = row[column]
            ##if this donor doesn't have this OTU, skip it
            if otuValue == 0:
                continue
            
            taxRaw = row[nameColumn].split(';') #split up taxonomic rank
            tax={}
            #populate the dictionary key= Kingdom value = bacteria
            for rank in taxRaw:
                rankName = rank.split('__')
                tax[rankName[0]]=rankName[1]
            #create new nodes    
            oldNode = sixteenS.head #start at head
            for level in sequence.TaxPyramid: 
                #if level is empty, add otu and otuValue to previous Node
                if tax[level]=='':
                    oldNode.otu.append(row[otuColumn]) 
                    oldNode.otuCount.append(otuValue)
                    break
                
                oldChildren = oldNode.children
                newNode = sequence.Node(tax[level], oldNode) #create new node with dictionary value and oldNode as parent
                newNode.taxonomiclevel=level
                # if newNode is already in oldChildren, set newNode = same child of old Node
                if newNode in oldChildren: 
                    indexOfSame = oldChildren.index(newNode)
                    newNode = oldChildren[indexOfSame]
                #else add it new node to parents children
                else:
                    oldNode.children.append(newNode) #add to list of children
                oldNode = newNode #set oldNode to newNode
                # if we are at the species level, add OTU and OTU value
                if level == sequence.Species:
                    oldNode.otu.append(row[otuColumn]) 
                    oldNode.otuCount.append(otuValue)
        sequences.append(sixteenS)
    for sequenceData in sequences:
        countCalculator(sequenceData)
    return sequences
    
    


def countCalculator(head):
    '''
    This function counts the total OTUs ending at this level and any below 
    ie. Firmicutes: 1230432 stored under the Node.count
    '''
    if isinstance(head, sequenceObject): ## if this is a sequence object, call this method on the head Node
        countCalculator(head.head)
    if isinstance(head, Node):
        sumVal = 0
        for otuValue in head.otuCount: ## sum values of OTU ending at this point
            sumVal+=otuValue
        if head.children:
            for child in head.children: ## for every child in children, count their values
                countCalculator(child) ## and sum it with the current Nodes sumVal total
                sumVal += child.count
        head.count = sumVal


def donorInitiator(databaseDirectory):
    '''
    This function intitiates all the donor objects pointed to the database passed in
    it returns a list of donor objects with appropriate donorIDs, 16s data, and SCFA data
    order is in the same provided in the donorList.csv file
    '''

    #Change to database directory and check for correct files, if they aren't there try again
    os.chdir(str(databaseDirectory))
    fileListCWD = os.listdir(os.getcwd())
    DonorFile = 'DonorListSample.csv'
    OTUtable = 'OTUtable.txt'
    SCFAData = 'SCFAtable.csv'
    requiredFiles = [DonorFile, OTUtable, SCFAData]
    for file in requiredFiles:
        if not file in fileListCWD:
            newDirectory = raiseFileError()
            donorInitiator(newDirectory)
            break
    
    #open donor ID list
    donorCSV=open('DonorListSample.csv', 'r')
    csvDonorReader= csv.reader(donorCSV, dialect=csv.excel_tab)
    
    #get list of donor numbers
    rownum = 0;
    donorNumList = []
    for row in csvDonorReader:
        rowInfo = row[0].split(',')
        if rownum == 0:
            donorHeader = row[0]
        else:
            donorNumList.append(int(rowInfo[0]))
        rownum+=1
        
    #create list of donor objects based on donor number list
    donorList=[]
    for donorNum in donorNumList:
        newDonor = Donor(donorNum)
        donorList.append(newDonor)
    
    #load sequence data and map it
    donorSequences = loadSequenceData()  
    taxMap = taxMapper(donorSequences)
    global taxonomicMap
    taxonomicMap.extend(taxMap)
    
    #load SCFA Data and assign it to appropriate donors
    fattyAcidData = loadSCFAData()
    for donor in donorList:
        if fattyAcidData.has_key(donor.donorID):
            donor.shortChainFattyAcids = fattyAcidData[donor.donorID]
            donor.countTotalScfa()
    #assign all sequences to appropriate donors (not efficient but n is small)
    for donor in donorList:
        for donorSequence in donorSequences:
            if donor.donorID == donorSequence.donor:
                donor.sequences.append(donorSequence)
    
    ## asign this list to the global variable donors
    global donors
    donors = donorList
    return donorList

def taxMapper(sequences):
    '''
    creates list of dictionaries for each taxonomic level with possible children
    '''
    taxMap = [{}, {}, {}, {}, {}, {}] ##create empty list for TaxMap with each dictionary representing Kingdom .. etc
    for sixteenS in sequences: ## go through each sequence
        nodes = Queue.Queue()
        curNode = sixteenS.head 
        children = curNode.children
        for child in children: ## add all initial kingdoms to queue
            nodes.put(child)
        while( not(nodes.empty()) ): #continue if no more nodes above species level
            curNode = nodes.get() 
            level = curNode.taxonomiclevel 
            levelNumber = sequence.TaxPyramid.index(level) ## get current taxonomic level of node
            dictionary = taxMap[levelNumber] ## get corresponding dicitonary for taxonomic level
            keyString = curNode.value
            ##gets set of children or creates new one if it doesn't exist
            if dictionary.has_key(keyString): 
                childSet = dictionary[keyString]
            else:
                dictionary[keyString] = sets.Set()
                childSet = dictionary[keyString]  
            ##gets list of current Nodes children and adds them to queue  
            childList = []
            for child in curNode.children:
                childList.append(child.value)
                ## only add if level is not species
                if child.taxonomiclevel != sequence.Species:
                    nodes.put(child)
            ## goes through list of children and adds them to the children set in dictionary       
            for child in childList:
                childSet.add(child)
    return taxMap

def loadSCFAData():
    '''
    This function takes in a SCFA table csv within the database folder. it returns a dictionary of donorID
    mapping to SCFA data. the acid data is itself a dictionary with {'SCFA", count} 
    '''
    #load SCFA Data table
    table = np.genfromtxt('SCFAtable.csv', dtype= None, delimiter = ',')
    
    SCFAdict = {}
    
    #get the header make a list of it
    header = table[0]
    fattyAcids = []
    for i in range(1, len(header)):
        fattyAcids.append(header[i])
    
    # get each donor's scfa data and enter it into dictionary as a dictionary with the name of each fatty acid as a key
    for i in range(1, len(table)):
        donorFattyAcids = table[i]
        donorID = 0
        acidData={}
        for j in range(0, len(donorFattyAcids)):
            val= donorFattyAcids[j]
            if j== 0:
                donorID = int(val)
            elif val == '':
                acidData[fattyAcids[j-1]]=float(0)
            else:
                acidData[fattyAcids[j-1]]=float(val)
    
        SCFAdict[donorID] = acidData
        
    return SCFAdict  
            

        
        
                
        
            
            
        