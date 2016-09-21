'''
PageRank.py
'''
import os
import math
from datetime import datetime

#---------------------------------------------------------------------#
# Global variables
#---------------------------------------------------------------------#
linkFileName = os.getcwd() + '/wt2g_inlinks.txt'
P 	= []
M 	= []
L 	= []
S 	= []
d 	= 0.85
maxCount = 50
InDict   = {}
OutDict  = {}
PRDict	 = {}
perplexityList = []
logList		= []
#---------------------------------------------------------------------#
# Function to read inlink file data
#---------------------------------------------------------------------#
def readInputFile(fileName):
	f = open(fileName,'r')
	for line in f:
		oneRecord = line
		findAllInLinksForAllNodes(oneRecord)
	f.close()

#---------------------------------------------------------------------#
# Function to find all inlinks for all nodes
#---------------------------------------------------------------------#
def findAllInLinksForAllNodes(record):
	recordList 	= record.split()
	currNode	= recordList[0]
	allInLinks	= recordList[1:]
	InDict.update({currNode:allInLinks})

#---------------------------------------------------------------------#
# Function to find all outlinks for all nodes
#---------------------------------------------------------------------#
def findAllOutlinksForAllNodes():
	for key in InDict.keys():
		for x in InDict[key]:
			if(OutDict.has_key(x)):
				OutDict[x] += 1 
			else:
				OutDict.update({x:1})

	for y in InDict.keys():
		if(y not in OutDict.viewkeys()):
			S.append(x)

#---------------------------------------------------------------------#
# Function all page rank for each page acording to algorithm given
#---------------------------------------------------------------------#
def findPageRankrWithConvergence():
	N 		= len(P)
	intiVal = 1.0/N
	converge= False
	newPR   = {}

	for p in P:
		PRDict.update({p:intiVal})	

	while(not converge):		
		sinkPR = 0

		for p in P:
			newPR.update({p:0})	

		for p in S:
			sinkPR += PRDict[p]

		for p in P:
			newPR[p] = (1-d)/N
			newPR[p] += d*sinkPR/N

			for q in InDict[p]:
		  		newPR[p] += d*PRDict[q]/OutDict[q]

		for p in P:
			PRDict[p] = newPR[p]

		newPerplexity = calculatePerplexity(PRDict)
		perplexityList.append(newPerplexity)

		if((4<=len(perplexityList)) and (perplexityList[-1] == perplexityList[-2] == perplexityList[-3] == perplexityList[-4])):
			converge = True

	return perplexityList

#---------------------------------------------------------------------#
# Function to calculate prepexlity for list of nodes
#---------------------------------------------------------------------#
def calculatePerplexity(PR):
	H = 0.0
	for k in PR.keys():
		if((math.log(PR[k],2)) > math.pow(10,-6)):
			H += PR[k]*(math.log(PR[k],2))
	H = (-1)*H
	perplexity = math.pow(2,H)
	return perplexity

#---------------------------------------------------------------------#
# Function to print page rank values in decreasing order
#---------------------------------------------------------------------#
def printInSortedOrder(dict):
	i =0
	for w in sorted(dict, key=dict.get, reverse=True):
  		if(i<maxCount):
  			print(w, round(dict[w],6))
  			i += 1

#---------------------------------------------------------------------#
# Function call to read inlink file
#---------------------------------------------------------------------#
print("Reading graph...")
readInputFile(linkFileName)
P = InDict.keys()
M = InDict.values()

#---------------------------------------------------------------------#
# Funciton to find all outlinks for each node : set of lists
#---------------------------------------------------------------------#
print("Finding outlinks in graph...")
findAllOutlinksForAllNodes()
L = OutDict.values()

#---------------------------------------------------------------------#
# Function call to run page rank algorithm
#---------------------------------------------------------------------#
print("Calculating page ranks in graph...")
perpList = findPageRankrWithConvergence()

#---------------------------------------------------------------------#
#							OUTPUTS
#---------------------------------------------------------------------#

#---------------------------------------------------------------------#
# 1. Printing number of nodes, inlinks, outslinks and sinks in graph
#---------------------------------------------------------------------#
print("1.all Nodes")
print(len(P))
print("  all inlink lists")
print(len(M))
print("  all outlink lists")
print(len(L))
print("  all sink nodes")
print(len(S))

#---------------------------------------------------------------------#
# 2. To create list of the perplexity values you obtain in each 
#    round until convergence as described above.
#---------------------------------------------------------------------#
print("2. creating perplexity list ")
filename = "perplexityList.txt"
work_dir = os.getcwd() + '/' + filename
f = open(work_dir,'w')
f.write("       fileName = " + filename + ' \n \n')
for l in perpList:
	f.write(str(l) + "\n")
f.close()

#---------------------------------------------------------------------#
# 3. To create a list of the document IDs of the top 50 pages as sorted
#    by PageRank, together with their PageRank values
#---------------------------------------------------------------------#
print("3. creating pagerank file")
fileName = 'pageRankListTop50.txt'
work_dir = os.getcwd() + '/' + fileName
i = 0
f = open(work_dir,'w')
dict = PRDict
f.write("       fileName = " + fileName + ' \n \n')
for w in sorted(dict, key=dict.get, reverse=True):
	if(i<maxCount):
		f.write(w + "	" + str(round(dict[w],6)) + "\n")
		i += 1
f.close()
#---------------------------------------------------------------------#
# 4. To create a list of the document IDs of the top 50 pages by 
#     in-link count, together with their in-link counts;
#---------------------------------------------------------------------#
print("4. creating inlink file")
fileName = 'InlinkListTop50.txt'
work_dir = os.getcwd() + '/' + fileName
y = .00165028727
i = 0
f = open(work_dir,'w')
dict = InDict
f.write("       fileName = " + fileName + ' \n \n')
for k in sorted(dict, key=lambda k: len(dict[k]), reverse=True):
	if(i<maxCount):
		f.write(k + "	" + str(len(dict[k])) + "\n")
		i += 1
f.close()

#---------------------------------------------------------------------#
# 5. the proportion of pages with no in-links (sources)
#---------------------------------------------------------------------#
t = 0.0
for k in InDict.viewvalues():
	if(len(k)==0):
		t += 1
x = t/float(len(P))
print("5. the proportion of pages with no in-links (sources) = " + str(x))


#---------------------------------------------------------------------#
# 6. To display the proportion of pages with no out-links (sinks)
#---------------------------------------------------------------------#
x = float(len(S))/float(len(P))
print("6. the proportion of pages with no out-links (sinks) = " + str(x))

#---------------------------------------------------------------------#
# 7. To display the proportion of pages whose PageRank is less 
#    than their initial, uniform values.
#---------------------------------------------------------------------#
t = 0.0
intiVal = 1.0/len(P)
for k in PRDict.viewvalues():
	if(k<intiVal):
		t += 1
x = t/float(len(P))
print("7. the proportion of pages whose PageRank is less than their initial = " + str(y))

printInSortedOrder(PRDict)
print(sum(PRDict.values()))

'''
execfile('C:/Users/anuk/anu/NEU_Study/FALL-2015/IR-Nada/Assignment/2/pageRankPart2.py')
'''	
