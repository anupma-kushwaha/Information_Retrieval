'''
PageRank.py
'''
import os


#---------------------------------------------------------------------#
#Global variables
#---------------------------------------------------------------------#
linkFileName = os.getcwd() + '/Part1_InputFile.txt'
P 	= []
M 	= []
L 	= []
S 	= []
d 	= 0.85
maxCount = 100
InDict   = {}
OutDict  = {}

#---------------------------------------------------------------------#
#Function to read inlink file data
#---------------------------------------------------------------------#
def readInputFile(fileName):
	f = open(fileName,'r')
	for line in f:
		oneRecord = line

		#Find all outlinks for each node : set of lists
		findAllInLinksForAllNodes(oneRecord)
	f.close()

	#Find all outlinks for each node : set of lists
	findAllOutlinksForAllNodes()

#---------------------------------------------------------------------#
#Function to find all inlinks for all nodes
#---------------------------------------------------------------------#
def findAllInLinksForAllNodes(record):
	global InDict
	recordList 	= record.split()
	currNode	= recordList[0]
	allInLinks	= recordList[1:]
	InDict.update({currNode:allInLinks})

#---------------------------------------------------------------------#
#Function to find all outlinks for all nodes
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
#Function all page rank for each page acording to algorithm given
#---------------------------------------------------------------------#
def findPageRankForAllPages(maxCount):
	global InDict
	global OutDict

	N 		= len(InDict)
	newPR	= {}
	PRDict	= {}
	initialValue = 1.0/N
	
	for p in P:
		newPR.update({p:0})

	for p in P:
		PRDict.update({p:initialValue})

	count = 0
	while (count<maxCount):
		sinkPR = 0

		for p in S:
			sinkPR += PRDict.get(p)

		for p in P:
			newPR[p] = (1-d)/N
			newPR[p] += (d*sinkPR)/N

			for q in InDict.get(p):
		  		newPR[p] += (d*PRDict[q])/OutDict[q]

		for p in P:
			PRDict[p] = newPR[p]

		count += 1

	return PRDict

#---------------------------------------------------------------------#
# Function to print page rank values in decreasing order
#---------------------------------------------------------------------#
def printInSortedOrder(dict):
	for w in sorted(dict, key=dict.get, reverse=True):
  		print w, round(dict[w],6)

#---------------------------------------------------------------------#
# Function to write data into output file
#---------------------------------------------------------------------#
def writeDataToFile(dict):
	work_dir = os.getcwd() + '/Part1_OutputPageRanks.txt'
	f = open(work_dir,'w')
	t = 'all pageranks with iteration ' + str(maxCount)
	f.write(t + "\n")
	for w in sorted(dict, key=dict.get, reverse=True):
			f.write(w + ",  " + str(round(dict[w],6)) + "\n")
	f.close()

#---------------------------------------------------------------------#
#Function call to read inlink file
#---------------------------------------------------------------------#
readInputFile(linkFileName)
P = InDict.keys()
M = InDict.values()
L = OutDict.values()

#---------------------------------------------------------------------#
#Function call run page rank algorithm
#---------------------------------------------------------------------#
print('all pageranks with iteration' , maxCount)
PRDict = findPageRankForAllPages(maxCount)
printInSortedOrder(PRDict)
writeDataToFile(PRDict)
print("sum of all pagerank = ",sum(PRDict.itervalues()))

'''
execfile('C:/Users/anuk/anu/NEU_Study/FALL-2015/IR-Nada/Assignment/2/pageRankPart1.py')
'''

