'''This file will be used to define the donor profile class
    numberID #donor ID, integer
    unsafeStudy #array of strings with possible study types donor is unable to contribute to, may be empty
    sequenceObject #sequenceObject top Node 
    shortChainFattyAcids #short chain fatty acid data structure
    materialAvailable #current material available from PooApp produced by the donor
    productionRate #rate of donor product being registered in the PooApp

'''

genderDict = {'Male': 'm', 'Female': 'f'}

class Donor:
    def __init__(self, donorID):
        self.donorID = donorID
        self.clinicalInfo = {'Abnormal Lab Results': '', 'Clinical Notes': '', 'Allergies': '', 'Diet': '', 'Other': ''}
        self.sequences = []
        self.shortChainFattyAcids={}
        self.productionRate = 0
        self.safetyRating = 0
        self.currentStudies = 0
        self.bmi=0
        self.waistCircumference = 0
        self.age = 0
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
        
    def getDonorID(self):
        return self.donorID
    
    def getClinicalInfo(self):
        return self.clinicalInfo
    
    def getSequences(self):
        return self.sequences
    
    def getShortChainFattyAcids(self):
        return self.shortChainFattyAcids
    
    def getProductionRate(self):
        return self.productionRate
    
    def getSafetyRating(self):
        return self.safetyRating
    
    def getCurrentStudies(self):
        return self.safetyRating
    
    def getBMI(self):
        return self.bmi
    
    def getWaistCircumference(self):
        return self.waistCircumference
      
    def getAge(self):
        return self.age
    
    def getGender(self):
        return self.gender
    
    def getProcessingStatus(self):
        return self.processingStatus
    
    def getShippingStatus(self):
        return self.shippingStatus
    
    def getMaterialAvailable(self):
        return self.materialAvailable
    
    def getSDI(self):
        return self.sdi
    def getJSD(self):
        return self.jsd
    
    def getFPROW(self):
        return self.fprow
    
    def getTotalSCFA(self):
        return self.totalSCFA 
     
    def getScreeningGroup(self):
        return self.screeningGroup
    
    
    
    