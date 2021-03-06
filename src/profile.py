'''This file will be used to define the donor profile class
    numberID #donor ID, integer
    unsafeStudy #array of strings with possible study types donor is unable to contribute to, may be empty
    sequenceObject #sequenceObject top Node 
    shortChainFattyAcids #short chain fatty acid data structure
    materialAvailable #current material available from PooApp produced by the donor
    productionRate #rate of donor product being registered in the PooApp

'''

genderDict = {'m': 'Male', 'f': 'Female', 'M': 'Male', 'F': 'Female'}
SafetyRatings={'approved': 1, 'conditional': 2, 'restricted': 3, 'rejected': 4}
import pandas as pd

class Donor:
    def __init__(self, donorID):
        self.donorID = int(donorID)
        self.clinicalInfo = {'Abnormal Lab Results': '', 'Clinical Notes': '', 'Allergies': '', 'Diet': '', 'Other': ''}
        self.sequences = []
        self.shortChainFattyAcids={}
        self.productionRate = 0
        self.safetyRating = ''
        self.currentStudies = 0
        self.bmi=None
        self.waistCircumference = None
        self.age = None
        self.gender = 'f'
        self.processingStatus = ''
        self.shippingStatus = ''
        self.materialAvailable = {}
        self.sdi = 0
        self.jsd = 0
        self.fprow = 0
        self.totalSCFA = 0.0
        self.screeningGroup = ''
        
    def countTotalScfa(self):
        '''
        method counts the total amount of SCFA detected in the SCFA dictionary
        '''
        sumVal = 0.0
        for acid  in self.shortChainFattyAcids.keys():
            value = self.shortChainFattyAcids[acid]
            sumVal=sumVal+value
        self.totalSCFA = sumVal
        
    def addInfo(self, infoDict):
        dictkeys = {'Safety Rating': self.setSafetyRating, 'Group': self.setScreeningGroup, 
                    'BMI': self.setBMI, 'WC': self.setWaistCircumference, 'Age': self.setAge, 'Gender': self.setGender, 
                    'Abnormal Lab Results': self.setClinicalInfo, 
                    'Clinical Notes': self.setClinicalInfo, 
                    'Allergies':self.setClinicalInfo, 'Diet': self.setClinicalInfo, 'Other': self.setClinicalInfo,
                    'Current Studies': self.setCurrentStudies}
        for key in dictkeys.keys():
            if infoDict.has_key(key):
                dictVal = infoDict[key]
                if isinstance(dictVal, unicode):
                    dictVal = str(dictVal)
                if pd.isnull(dictVal):
                    continue
                setFunc = dictkeys[key]
                if setFunc == self.setClinicalInfo:
                    setFunc(key, dictVal)
                else:
                    setFunc(dictVal)
        
    def getDonorID(self):
        return self.donorID

    
    def getClinicalInfo(self):
        return self.clinicalInfo
    
    def setClinicalInfo(self, key, val):
        if not self.clinicalInfo.has_key(key):
            return
        self.clinicalInfo[key]=val
    
    def getSequences(self):
        return self.sequences
    
    def getShortChainFattyAcids(self):
        return self.shortChainFattyAcids
    
    def getProductionRate(self):
        return self.productionRate
    
    def getSafetyRating(self):
        safetyNum = self.safetyRating
        for key,value in SafetyRatings.items():
            if value == safetyNum:
                return key
    
    def setSafetyRating(self, val):
        val=val.lower()
        if SafetyRatings.has_key(val):
            self.safetyRating = SafetyRatings[val]
    
    def getCurrentStudies(self):
        return long(self.currentStudies)
    
    def setCurrentStudies(self, val):
        self.currentStudies = val
    
    def getBMI(self):
        if self.bmi:
            return float(self.bmi)
        else:
            return self.bmi
    
    def setBMI(self, val):
        self.bmi = val
    
    def getWaistCircumference(self):
        if self.waistCircumference:
            return float(self.waistCircumference)
        else:
            return self.waistCircumference
    
    def setWaistCircumference(self, val):
        self.waistCircumference = val
      
    def getAge(self):
        if self.age:
            return int(self.age)
        else:
            return self.age
    
    def setAge(self, val):
        self.age = val
        
    def getGender(self):
        return self.gender
    
    def setGender(self, val):
        if genderDict.has_key(val):
            self.gender = genderDict[val]
    
    def getProcessingStatus(self):
        return self.processingStatus
    
    def setProcessingStatus(self, val):
        self.processingStatus = val
    
    def getShippingStatus(self):
        return self.shippingStatus
    
    def getMaterialAvailable(self):
        return self.materialAvailable
    
    def displayMaterialAvailable(self):
        newDict = self.materialAvailable
        if not newDict or not isinstance(newDict, dict):
            return ""
        newDictString = {}
        for key in newDict.keys():
            curList = []
            for item in newDict[key].keys():
                curItemVal = newDict[key][item]
                curItemCount = curItemVal[0]
                unitType = curItemVal[1]
                if unitType == "unit":
                    unitType = unitType +"s"
                elif not unitType:
                    unitType = ""
                itemString = item + ": " + str(curItemCount) + " " + unitType
                curList.append(itemString)
            newDictString[key] = curList
        displayString = ''
        for key in newDictString.keys():
            displayString = displayString + key + ": "
            curList = newDictString[key]
            for item in curList:
                displayString = displayString + item + ", "
            displayString = displayString[:-2]
            displayString = displayString + "\n"
        return displayString
    def getSDI(self):
        return float(self.sdi)
    def getJSD(self):
        return float(self.jsd)
    
    def getFPROW(self):
        return float(self.fprow)
    
    def getTotalSCFA(self):
        return float(self.totalSCFA)
     
    def getScreeningGroup(self):
        return self.screeningGroup
    
    def setScreeningGroup(self, val):
        self.screeningGroup = val   
        
    def averageDonorSDI(self):
        if not self.sequences:
            return
        totalSDI = 0
        count = 0
        for sequenceObject in self.sequences:
            count = count +1
            totalSDI = totalSDI + sequenceObject.sdi
        self.sdi = totalSDI/count
        
    def averageDonorPrau(self):
        if not self.sequences:
            return
        totalPrau = 0
        count = 0
        for sequenceObject in self.sequences:
            count = count +1
            totalPrau = totalPrau + sequenceObject.prausnitzii
        self.fprow = totalPrau/count
        
        

                     
    
    
    