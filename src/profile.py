'''This file will be used to define the donor profile class
    numberID #donor ID, integer
    unsafeStudy #array of strings with possible study types donor is unable to contribute to, may be empty
    sequenceObject #sequenceObject top Node 
    shortChainFattyAcids #short chain fatty acid data structure
    materialAvailable #current material available from PooApp produced by the donor
    productionRate #rate of donor product being registered in the PooApp

'''

class Donor:
    def __init__(self, donorID):
        self.donorID = donorID
        self.clinicalInfo = None
        self.sequences = []
        self.shortChainFattyAcids=[]
        self.materialAvailable = 0
        self.productionRate = 0
        
    
    