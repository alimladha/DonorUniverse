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
        self.clinicalInfo = None
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
        
    def countTotalScfa(self):
        '''
        method counts the total amount of SCFA detected in the SCFA dictionary
        '''
        sumVal = 0.0
        for acid  in self.shortChainFattyAcids.keys():
            value = self.shortChainFattyAcids[acid]
            sumVal=sumVal+value
        self.totalSCFA = sumVal
    
    