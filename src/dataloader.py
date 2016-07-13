import os
import numpy as np
import sequence
from sequence import Node, sequenceObject
from profile import Donor
import Queue, sets
import pandas as pd
from PyQt4 import QtCore, QtGui
import sys
import googleDataSearcher
import bioinformatics
import jsdCalculator

taxonomicMap = [] ##global taxonomic Map 
donors=[] ##global list of donors
screeningGroups =sets.Set() ##global set of all screening groups
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
    try:
        table= np.genfromtxt('OTUtable.txt', dtype = None, skip_header=1)
    except:
        raiseFileCannotBeOpenedError()
        sys.exit()
    #loadOTU header
    txt=open('OTUtable.txt')
    header=txt.readline().split()
    
    #normalize OTU Data
    totalCounts = [0]*(len(header))
    for column in xrange(1, len(header)-1):
        for row in table:    
            curCount = row[column]
            totalCounts[column] = totalCounts[column] + curCount
    
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
        sixteenS.totalCount = totalCounts[column]
        nameColumn = len(header)-1 #define column where taxonomic data is located
        otuColumn = 0 #define column where OTU ID is located
        prausnitzii = 0
        
        for row in table: #iterate through each OTU
            otuValue = float(row[column])/float(totalCounts[column])
            ##if this donor doesn't have this OTU, skip it
            if otuValue == 0:
                continue
            
            taxRaw = row[nameColumn].split(';') #split up taxonomic rank
            tax={}
            #populate the dictionary key= Kingdom value = bacteria
            for rank in taxRaw:
                rankName = rank.split('__')
                tax[rankName[0]]=rankName[1]
                if rankName[1] == 'prausnitzii':
                    prausnitzii = prausnitzii + otuValue
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
        sixteenS.sdi = calculateSDI(sixteenS)
        sixteenS.prausnitzii = prausnitzii
        sequences.append(sixteenS)
    for sequenceData in sequences:
        countCalculator(sequenceData)
    calculateSDIAverage(sequences)
    calculatePrauAverage(sequences)
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


def donorInitiator( driveData, otherData, databaseDirectory = None, credentialCWD = None):
    '''
    This function intitiates all the donor objects pointed to the database passed in
    it returns a list of donor objects with appropriate donorIDs, 16s data, and SCFA data
    order is in the same provided in the donorList.csv file
    '''
    if not credentialCWD:
        credentialCWD = os.getcwd() # gets directory where credential file is stored
    
    ## if no database directory is given, get data from google drive
    if databaseDirectory == None:
        try:
            returnValue = googleDataSearcher.loadDonorData()
        except:
            raiseGoogleDriveError()
        global screeningGroups
        screeningGroups = returnValue[0]
        donors = returnValue[1]
        if otherData:
            loadOtherData(donors)
        return donors
    #Change to database directory and check for correct files, if they aren't there try again
    try:
        os.chdir(str(databaseDirectory))
    except OSError:
        sys.exit()
    except:
        sys.exit()
    
    fileListCWD = os.listdir(os.getcwd())
    fileCWD = os.getcwd()
    OTUtable = 'OTUtable.txt'
    SCFAData = 'SCFAtable.csv'
    DonorInfoFile = 'DonorData.xlsx'
    
    requiredFiles = []
    
    if driveData == False:
        requiredFiles.append(DonorInfoFile)
    
    if otherData == True:
        requiredFiles.append(OTUtable)
        requiredFiles.append(SCFAData)
        
    for requiredFile in requiredFiles:
        if not requiredFile in fileListCWD:
            newDirectory = raiseFileError()
            return donorInitiator(driveData, otherData, newDirectory, credentialCWD)
        
    if driveData == True:
        os.chdir(credentialCWD)
        try:
            returnValue = googleDataSearcher.loadDonorData()
        except:
            raiseGoogleDriveError()
        os.chdir(fileCWD)
        global screeningGroups
        screeningGroups = returnValue[0]
        donors = returnValue[1]
        if otherData:
            loadOtherData(donors)
        return donors
         
    #get donors from DonorInfoFile, and collect metadata
    try:
        table = pd.read_excel(DonorInfoFile)
    except:
        raiseFileCannotBeOpenedError()
    donorNumList = []
    infoArrays = []
    for row in table.itertuples():
        try:
            donorNumList.append(row.Donor)
            infoDict = {'Safety Rating': row.SafetyRating, 'Group': row.Group, 'BMI': row.BMI, 'WC': row.WC,
                    'Age': row.Age, 'Gender': row.Gender, 'Abnormal Lab Results': row.AbnormalLabResults, 
                    'Clinical Notes': row.ClinicalNotes, 'Allergies': row.Allergies, 'Diet': row.Diet,
                    'Other' :row.Other}
        except:
            raiseFileCannotBeOpenedError()
        global screeningGroups
        if not pd.isnull(row.Group):
            screeningGroups.add(str(row.Group))
        infoArrays.append(infoDict)
        
    #create list of donor objects based on donor number list, add appropriate data
    donorList=[]
    for donorNum, donorInfo in zip(donorNumList,infoArrays):
        newDonor = Donor(donorNum)
        newDonor.addInfo(donorInfo)
        donorList.append(newDonor)
    if otherData:
        loadOtherData(donorList)
    return donorList

def loadOtherData(donorList):
    #load sequence data and map it
    try:
        donorSequences = loadSequenceData() 
    except:
        raiseFileCannotBeOpenedError() 
    taxMapper(donorSequences)
    
    #load SCFA Data and assign it to appropriate donors
    fattyAcidData = loadSCFAData()
    for donor in donorList:
        if fattyAcidData.has_key(donor.donorID):
            donor.shortChainFattyAcids = fattyAcidData[donor.donorID]
            donor.countTotalScfa()
    #set SCFA Average
    setSCFAAverage(donorList)
    
    #assign all sequences to appropriate donors (not efficient but n is small)
    for donor in donorList:
        for donorSequence in donorSequences:
            if donor.donorID == donorSequence.donor:
                donor.sequences.append(donorSequence)
    

    for donor in donorList:
        donor.averageDonorSDI()
        donor.averageDonorPrau()
        
    jsdCalculator.importJSDFromPickle(donorList)
       
    ## assign this list to the global variable donors
    global donors
    donors = donorList

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
    global taxonomicMap
    taxonomicMap = taxMap
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

def setSCFAAverage(donors):
    '''
    This function goes through a list of donors, adds all the total SCFA counts if they aren't zero,
    and averages them. It then assigns it to the global variable totalSCFAaverage
    '''
    sumSCFA = 0.0
    count = 0
    for donor in donors:
        donorSCFAtotal = donor.getTotalSCFA()
        if donorSCFAtotal > 0:
            sumSCFA = sumSCFA + donorSCFAtotal
            count = count+1
    global totalSCFAAverage
    totalSCFAAverage = sumSCFA/count

def quitApp():
    QtGui.QApplication.quit()
    
def raiseLimitError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('Something is wrong with the upper and lower limits set on one of your searches!'))
    error.exec_()
    raise ValueError('Limit Problem')

def raiseFileError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('File directory chosen does not include required files'))
    error.exec_()
    return showFileOpener()

def showFileOpener():
    databaseDirectory = QtGui.QFileDialog.getExistingDirectory(None,QtCore.QString("Open Database Directory"),"/home", QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
    return databaseDirectory

def raiseFileCannotBeOpenedError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('Files given cannot be opened'))
    error.exec_()
    
def raiseGoogleDriveError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('Error Getting Data from Google Drive'))
    error.exec_()
    raise ValueError("No Google Data")

def calculateSDI(sequence):
    otuDict = {}
    head = sequence.head
    q = Queue.Queue()
    q.put(head)
    while not q.empty():
        curNode = q.get()
        otus = curNode.otu
        otuCount = curNode.otuCount
        for otu, val in zip(otus, otuCount):
            otuDict[otu] = val * sequence.totalCount
        children = curNode.children
        for child in children:
            q.put(child)
    sdi = bioinformatics.sdi(otuDict)
    return sdi
    
def calculateSDIAverage(sequences):
    totalSDI = 0
    count = 0
    for sequenceObject in sequences:
        totalSDI = totalSDI + sequenceObject.sdi
        count = count + 1
    global sdiAverage
    sdiAverage =  totalSDI/count

def calculatePrauAverage(sequences):
    totalPrau = 0
    count = 0
    for sequenceObject in sequences:
        totalPrau = totalPrau + sequenceObject.prausnitzii
        count = count + 1
    global fprowAverage
    fprowAverage =  totalPrau/count
    
        
    
    
        