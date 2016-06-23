'''
 Everything in this file performs searches through already loaded data
'''

from Queue import PriorityQueue, Queue
from functools import total_ordering
from sequence import TaxPyramid
import math
from PyQt4 import QtCore, QtGui
from dataloader import sdiAverage,jsdAverage,fprowAverage, totalSCFAAverage

donorsWithSequences = [] ##global variable with all donors who have sequence Data
SafetyRatings={'Approved': 1, 'Conditional': 2, 'Restricted': 3, 'Rejected': 4, 'Conditional or better':5, 'Restricted or better': 6}

@total_ordering
class DonorRankNode:
    '''
    class associates donor IDs with counts, this is used for sorting
    the greater the value, the lower it is considered ie when sorted normally [ {ID, 51}, {ID, 30}, {ID, 20} ]
    '''
    def __init__(self, idNumber, count):
        self.idNumber = idNumber
        self.count = count
    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.count == other.count
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        return self.count < other.count
    
    def __lt__(self, other):
        return self.count > other.count
    
    def getId(self):
        return self.idNumber
    
    def getCount(self):
        return self.count
    
    def toString(self):
        return str(self.idNumber) + ": " + str(self.count)
    
    def sameID(self,other):
        return self.idNumber == other.idNumber
    
    
    
def ranker(donors):
    '''
    takes list of donors, finds those with sequences, assigns those to donors with sequences
    then it goes through and for each hit, adds a dictionary entry for the corresponding taxonomic level
    with label as key (ie. firmicutes) and donor rank objects in a priority queue as values
    then returns this dictionary
    Function requires list of donor profiles that include some properly formatted sequence data
    '''
    sequences=[]
    searchList = [{}, {}, {}, {}, {}, {}, {}]
    global donorsWithSequences
    del donorsWithSequences[:]
    for donor in donors:
        if donor.sequences:
            global donorsWithSequences
            donorsWithSequences.append(donor.donorID)
            for sequenceData in donor.sequences:
                sequences.append(sequenceData)
    if sequences:
        for sequenceData in sequences:
            donorID = sequenceData.donor
            currentNode = sequenceData.head
            q = Queue()
            for child in currentNode.children:
                q.put(child)
            while not q.empty():
                currentNode = q.get()
                donorObject = DonorRankNode(donorID, currentNode.count)
                keyValue = currentNode.value
                taxLevel = currentNode.taxonomiclevel
                taxNumber = TaxPyramid.index(taxLevel)
                levelDict = searchList[taxNumber]
                if keyValue not in levelDict:
                    levelDict[keyValue] = PriorityQueue()
                keyPQ = levelDict[keyValue]
                keyPQ.put(donorObject)
                for child in currentNode.children:
                    q.put(child)     
    return searchList
    
def topMatch(weight, value, taxLevel, searchList):
    '''
    given a weight, label, taxonomic Level of the label, and the searchlist iten from ranker,
    returns the top match donor rank object
    '''
    dict = searchList[TaxPyramid.index(taxLevel)]
    pq = dict[value]
    if weight>0:
        match = pq.get()
    if weight<0:
        while not pq.empty():
            match = pq.get()
    return match

def topKMatches(weight, value, taxLevel, searchList):
    '''
    given a weight, label, taxonomic Level of the label, and the searchlist item from ranker,
    returns a list of ranked donors for ALL donors with sequences INCLUDING ZERO VALUES
    '''
    dictItem = searchList[TaxPyramid.index(taxLevel)]
    if not dictItem.has_key(value):
        return []
    pq = dictItem[value]
    returnList = []
    if weight>0:
        while not pq.empty():
            returnList.append(pq.get())
    if weight<0:
        reverseList = []
        donorsWithoutHits = []
        while not pq.empty():
            reverseList.append(pq.get())
        for donor in donorsWithSequences:
            if not listDonorRankSearcher(reverseList, donor):
                donorsWithoutHits.append(DonorRankNode(donor, 0))
        for donor in donorsWithoutHits:
            reverseList.append(donor)
        while reverseList:
            returnList.append(reverseList.pop())
    return returnList
        
def search(searchDict, donors):
    '''
    takes in a dictionary of searches formatted as such {label: (taxLevel, weight)} ie {Firmicutes: (Phylumn, 2)}
    returns list of lists with each list in the overall structure containing the searches in order

    '''
    searchList = ranker(donors)
    result = []
    weights = []
    searches = []
    for key in searchDict.keys():
        searches.append(key)
        value = key
        tupVal = searchDict[key]
        taxLevel = tupVal[0]
        weight = tupVal[1]
        weights.append(math.fabs(weight))
        orderedDonors = topKMatches(weight, value, taxLevel, searchList)
        result.append(orderedDonors)
    totalScores = {}
    for searchResult in range(0, len(result)):
        counter = 1
        for donorRank in result[searchResult]:
            idNum = donorRank.idNumber
            rank = counter
            counter=counter+1
            if not totalScores.has_key(idNum):
                totalScores[idNum]=rank*weights[searchResult]
            else:
                curScore = totalScores[idNum]
                curScore = curScore + rank*weights[searchResult]
                totalScores[idNum] = curScore
    donorRankList = []
    for donorKey in totalScores.keys():
        idNum = donorKey
        weightedScore = totalScores[idNum]
        donorRankList.append(DonorRankNode(idNum, weightedScore))
    donorRankList.sort(reverse=True)
    return result
        
def SCFAranker(donors, fattyAcid, weight):
    '''
    given a fattAcid, returns a list of ordered donor objects w.r.t that fatty acid
    '''
    fattyAcidPQ = PriorityQueue()
    for donor in donors:  
        acidData = donor.shortChainFattyAcids
        if acidData:
            if acidData.has_key(fattyAcid):
                fattyAcidPQ.put(DonorRankNode(donor.donorID, acidData[fattyAcid]))
            else:
                fattyAcidPQ.put(DonorRankNode(donor.donorID, 0.0))
    fattyAcidList=[]
    while not fattyAcidPQ.empty():
        fattyAcidList.append(fattyAcidPQ.get())
    if weight>0.0:
        return fattyAcidList
    else:
        reverseList = []
        while fattyAcidList:
            reverseList.append(fattyAcidList.pop())
        return reverseList
        
def fattyAcidSearcher(donors, searchList):
    '''
    given a bunch of searches in a list: [(acid1, weight1), (acid2, weight2)] 
    returns list of lists with each list corresponding to search results in order
    '''
    searchResult = []
    for searchTup in searchList:
        acid = searchTup[0]
        weight = searchTup[1]
        result = SCFAranker(donors, acid, weight)
        searchResult.append(result)
    return searchResult
    
def listDonorRankSearcher(donorList, donorID):
    '''
    given a list of donors and a desired donorID, returns true if donorList contains an object with donorID
    otherwise returns false
    '''
    for donor in donorList:
        if donor.idNumber == donorID:
            return True
    return False

def findMatches(form, answers, donors):
    donorMatches = []
    for donor in donors:
        if(answers[form.safetyRatingCheck]):
            if not isSafe(answers[form.safetyRatingCombo], donor):
                continue
        if(answers[form.bmiCheck]):
            wantLL = answers[form.bmiLLCheck]
            wantUL = answers[form.bmiULcheck]
            ll = answers[form.bmiLLSpin]
            ul = answers[form.bmiULSpin]
            if not meetsRange(wantLL, ll, wantUL, ul, donor.bmi):
                continue
        if(answers[form.waistCheck]):
            wantLL = answers[form.waistLLCheck]
            wantUL = answers[form.waistULCheck]
            ll = answers[form.waistLLSpin]
            ul = answers[form.wasitULSpin]
            if not meetsRange(wantLL, ll, wantUL, ul, donor.waistCircumference):
                continue
        if(answers[form.ageCheck]):
            wantLL = answers[form.ageLLCheck]
            wantUL = answers[form.ageULCheck]
            ll = answers[form.ageLLSpin]
            ul = answers[form.ageULSpin]
            if not meetsRange(wantLL, ll, wantUL, ul, donor.age):
                continue
        if(answers[form.genderCheck]):
            wantMale = answers[form.maleRadio]
            wantFemale = answers[form.femaleRadio]
            if not rightGender(wantMale, wantFemale, donor.gender):
                continue
        if(answers[form.processStatusCheck]):
            if not processCheck(answers[form.processStatusCombo], donor):
                continue
        if(answers[form.shippingCheck]):
            if not shippingCheck(answers[form.processStatusCombo, donor]):
                continue
        if(answers[form.materialCheck]):
            type_1 = answers[form.materialTypeCombo_1]
            type_2 = answers[form.materialTypeCombo_2]
            type_3 = answers[form.materialTypeCombo_3]
            if not(type_1) and not(type_2) and not(type_3):
                raiseMaterialError()
            val_1 = answers[form.unitsSpin_1]
            val_2 = answers[form.unitsSpin_2]
            val_3 = answers[form.unitsSpin_3]
            typVal = [(type_1,val_1), (type_2, val_2), (type_3, val_3)]
            if not materialCheck(typVal, donor):
                continue
                
        if(answers[form.sdiCheck]):
            respectToAverage = answers[form.sdiCombo]
            if not averageCheck(respectToAverage, sdiAverage, donor.sdi):
                continue
        if(answers[form.jsdCheck]):
            respectToAverage = answers[form.jsdCombo]
            if not averageCheck(respectToAverage, jsdAverage, donor.jsd):
                continue
        
def isSafe(safetyRating, donor):
    safetyRatingNum = SafetyRatings[safetyRating]
    if safetyRatingNum < 5:
        return safetyRatingNum == donor.safetyRating
    elif safetyRatingNum == 5:
        return donor.safetyRating < 3
    elif safetyRatingNum == 6:
        return donor.safetyRating < 4
def meetsRange(wantLL, ll, wantUL, ul, donorValue):
    if wantLL == False and wantUL == False:
        raiseLimitError()
    if wantLL and wantUL:
        if ll>ul or ll==ul:
            raiseLimitError()
        else:
            return (donorValue>=ll and donorValue<=ul)
    elif wantLL:
        return donorValue>=ll
    elif wantUL:
        return donorValue<=ul

def raiseLimitError():
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('Something is wrong with the upper and lower limits set on one of your searches!'))
    error.exec_()
    raise ValueError('Limit Problem')

def rightGender(wantMale, wantFemale, gender):
    if not(wantMale) and not(wantFemale):
        error = QtGui.QErrorMessage()
        error.showMessage(QtCore.QString('No gender selected'))
        error.exec_()
        raise ValueError('Gender not selected')   
    elif wantMale:
        return gender == 'm'
    elif wantFemale:
        return gender =='f' 
    
def processCheck(status, donor):
    return donor.processingStatus == status

def shippingCheck(status, donor):
    return donor.shippingStatus == status

def raiseMaterialError():
    error=QtGui.QErrorMessage()
    error.showMessage(QtCore.QString('No Requested Type of Material'))
    error.exec_()
    raise ValueError('No Requested Type of Material')

def materialCheck(typeValList, donor):
    materialAvailable = donor.materialAvailable
    donorPasses = True
    for typeVal in typeValList:
        type = typeVal[0]
        val = typeVal[1]
        if not type:
            continue
        elif not materialAvailable.has_key(type):
            continue
        else:
            if materialAvailable[type]<val:
                donorPasses=False
    return donorPasses

def averageCheck(respectToAverage, average, value):
    if respectToAverage == 'Above Average':
        return value>average
    elif respectToAverage == 'Below Average':
        return value<average
        
            
        
    

        
    
    
    
    
        


                