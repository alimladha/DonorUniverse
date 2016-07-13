'''
Created on Jul 13, 2016

@author: alim
'''
from bioinformatics import jensen_shannon_from_dict
import Queue
import dataloader
import cPickle as pickle
import datetime
import sets
def calculateJSD(sequences):
    otuDicts = convertSequenceToDict(sequences)
    for i in xrange(len(otuDicts)):
        otuDict = otuDicts[i]
        jsdTotal = 0
        counter = 0
        for j in xrange(len(otuDicts)):
            if not i==j:
                jsd = jensen_shannon_from_dict(otuDict, otuDicts[j])
                jsdTotal = jsdTotal + jsd
                counter = counter+1
        medianJSD = jsdTotal/counter
        sequences[i].jsd = medianJSD
        
        
def calculateDonorJSD(donorList):
    sequences = []
    jsdDict = {}
    for donor in donorList:
        if donor.sequences:
            for sequence in donor.sequences:
                sequences.append(sequence)
    calculateJSD(sequences)
    jsdSumTotal = 0
    jsdDonorCount = 0
    for donor in donorList:
        jsdTotal = 0
        counter = 0
        if donor.sequences:
            for sequence in donor.sequences:
                jsdTotal = jsdTotal + sequence.jsd
                counter = counter +1
            jsdAvg = jsdTotal/counter
            jsdDict[donor.getDonorID()] = jsdAvg
            jsdSumTotal = jsdSumTotal + jsdAvg
            jsdDonorCount = jsdDonorCount +1
    jsdAverage = jsdSumTotal/jsdDonorCount
    jsdDict['Average'] = jsdAverage
    jsdDict['Date'] = datetime.date.today()
    pickle.dump(jsdDict, open("jsd.p", "wb"))
    print "pickled"
    return jsdDict
    
    
def importJSDFromPickle(donorList):
    try:
        jsdDict = pickle.load(open("jsd.p", "rb"))
    except:
        print "no pickle"
        jsdDict = calculateDonorJSD(donorList)
        
    margin= datetime.timedelta(days = 7)
    today = datetime.date.today()
    if jsdDict['Date']+margin<today:
        jsdDict = calculateDonorJSD(donorList)
    for donor in donorList:
        donorID = donor.getDonorID()
        if jsdDict.has_key(donorID):
            jsd = jsdDict[donorID]
            donor.jsd = jsd 
    dataloader.jsdAverage = jsdDict['Average']           
            
def convertSequenceToDict(sequences):
    otuKeys = sets.Set()
    otuDicts = []
    for sequence in sequences:
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
                otuKeys.add(otu)
            children = curNode.children
            for child in children:
                q.put(child)
        otuDicts.append(otuDict)
    for otuDict in otuDicts:
        for otuKey in otuKeys:
            if not otuDict.has_key(otuKey):
                otuDict[otuKey] = 0
    return otuDicts
    

