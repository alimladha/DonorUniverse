''' This class is used to store 16S sequencing data with each level (kingdom, phylum, class....) represented with a total count and ending OTUs to identify leaf nodes


class Node
    name #name of node ex. firmicutes
    child #child node
    parent #parent node if applicable
    total #total count of OTUs at this level
    otu #list of OTUs ending on this level
    otuCount #list of counts of OTUs ending on this level, indices match otu list
    
    
class sequenceObject
    head #topNode
    
 
    func shannonDiversity(Node) #calculates shannon diversity index

    func averageDistanceJSD(Node) #calculates average distance using JSD

    func speciesEnrichment(Node) #calculates speciesEnrichment
    '''
#setup key variables (Kingdom, Phylum, etc..)
Kingdom = 'k'
Phylum = 'p'
Class = 'c'
Order = 'o'
Family = 'f'
Genus = 'g'
Species = 's'

TaxPyramid = [Kingdom, Phylum, Class, Order, Family, Genus, Species]

class Node:
    count = 0;    ##default count is zero
    def __init__(self, value = None, parent =None):
        self.children = [] ## None if child isn't passed in
        self.parent = parent ##None if parent isn't passed in
        self.otu = [] ## always empty list
        self.otuCount = [] ##always empty list
        self.value = value ## None if value isn't passed (only for sixteenS head)
        self.taxonomiclevel = None ##taxonomic level set during data import
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.value == other.value)

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def toString(self):
        if self.value == None:
            string = 'head'
        else:
            string = self.value
        outString = string+ ":"
        for child in self.children:
            outString += child.value + ","
        return outString
class sequenceObject:
    def __init__(self):
        self.head = Node() ##sequence object just contains head Node (ie. no parent)
        self.donor = None
        self.sample = None
        


        
        