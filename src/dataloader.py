import os
import numpy as np
import sequence
from sequence import Node, sequenceObject

#Change to database directory
os.chdir('..') 
os.chdir('Databases')

#load OTU data as table
table= np.genfromtxt('OTUtable.txt', dtype = None, skip_header=1)

#loadOTU header
txt=open('OTUtable.txt')
header=txt.readline().split()

#for each donor create a sequence object
sequences = [] # create empty list of sequenceObjects
for column in xrange(1, len(header)-1):
    sixteenS = sequence.sequenceObject() #create sequence object
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
            # if newNode is already in oldChildren, set newNode = same child of old Node
            if newNode in oldChildren: 
                indexOfSame = oldChildren.index(newNode)
                newNode = oldChildren[indexOfSame]
            #else add it new node to parents children
            else:
                oldNode.children.append(newNode) #add to list of children
            oldNode = newNode #set oldNode to newNode
    sequences.append(sixteenS)
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

            
    

        
                
        
            
            
        