# This class is used to store 16S sequencing data with each level (kingdom, phylum, class....) represented with a total count and ending OTUs to identify leaf nodes
#
#
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
    