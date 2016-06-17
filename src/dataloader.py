import os
import numpy as np
import sequence
from sequence import Node, sequenceObject
import csv
from profile import Donor
import Queue, sets

taxonomicMap = []

def loadSequenceData():

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
    
    

'''
This function counts the total OTUs ending at this level and any below ie. Firmicutes: 1230432 stored under the Node.count
'''
def countCalculator(head):
    if isinstance(head, sequenceObject):
        countCalculator(head.head)
    if isinstance(head, Node):
        sumVal = 0
        for otuValue in head.otuCount:
            sumVal+=otuValue
        if head.children:
            for child in head.children:
                countCalculator(child)
                sumVal += child.count
        head.count = sumVal


def donorInitiator():
    #Change to database directory
    os.chdir('..') 
    os.chdir('Databases')
    
    #open donor ID list
    donorCSV=open('DonorListSample.csv', 'r')
    csvDonorReader= csv.reader(donorCSV, dialect=csv.excel_tab)
    
    #get list of donor numbers
    rownum = 0;
    donorNumList = []
    for row in csvDonorReader:
        if rownum == 0:
            donorHeader = row[0]
        else:
            donorNumList.append(int(row[0]))
        rownum+=1
    #create list of donor objects based on donor number list
    print donorNumList
    donorList=[]
    for donorNum in donorNumList:
        newDonor = Donor(donorNum)
        donorList.append(newDonor)
    
    #load sequence data and map it
    donorSequences = loadSequenceData() 
    taxMap = taxMapper(donorSequences)
    global taxonomicMap
    taxonomicMap.extend(taxMap)
    
    #assign all sequences to appropriate donors (not efficient but n is small)
    for donor in donorList:
        for donorSequence in donorSequences:
            if donor.donorID == donorSequence.donor:
                donor.sequences.append(donorSequence)
    
    
    return donorList
'''
creates list of dictionaries for each taxonomic level with possible children
'''
def taxMapper(sequences):
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

        
        
                
        
            
            
        