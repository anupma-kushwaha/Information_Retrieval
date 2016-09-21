__author__ = 'Anupma Kushwaha'

from math import log
import collections, os, sys, operator, math

#--------------------------------------------------------------------------------
#  Setting variables
#--------------------------------------------------------------------------------
cacmIndex = ["1","2","3"] # for "12,"13","19"
N = len(cacmIndex)
refrelFile = "cacm.rel.txt"
queryResFile = "Query.txt"
outputFileName = "results.txt"
maxRecord  = 100
MAP = 0.0
K = 20

#--------------------------------------------------------------------------------
#  Functions
#--------------------------------------------------------------------------------
def readRelRefFile(fileName):
	str = list()
	work_dir = os.getcwd() + "/"
 	fileName = work_dir + fileName
	f = open(fileName,'r')
	for line in f:
		line 	= line.replace("\n","").split(" ")
		qId		= line[0]
		q0 		= line[1]
		docId 	= line[2]
		rel 	= line[3]
		s = qId.strip() + "," + q0.strip() + "," + docId.strip() + "," + rel
		str.append(s)
	f.close()
	return str

def readQueryResults(fileName):
	str = list()
	work_dir = os.getcwd() + "/"
 	fileName = work_dir + fileName
	f = open(fileName,'r')
	for line in f:
		line 	= line.split(" ")
		qId 	= line[0]
		q0 		= line[1]
		docId 	= line[2]
		rank 	= line[3]
		score 	= line[4].replace("\n","")
		s = qId.strip() + "," + q0.strip() + "," + docId.strip() + "," + rank.strip()  + "," + score.strip()
		str.append(s)
	f.close()
	return str


def processForNQueries(N,totRecord,QueryResSet,cacmRes):
	i = 0;
	resultSet = list()
	PatK = [0]*N
	AVP = [0]*N
	map = 0.0

	while(i<N):

		queryNo = cacmIndex[i]
		
		# Cacm matches and Query result set matches form previous hw results for given query
		cacmMatches = list()
		for s in cacmRes:
			if(queryNo in s.split(",")[0]): 
				cacmMatches.append(s)

		queryMatches = list()
		for s in QueryResSet:
			if(queryNo in s.split(",")[0]): 
				queryMatches.append(s)

		relevance = 0.0
		j = 1
		dcg = 0.0
		avg = 0.0
		cacmLen = len(cacmMatches)
		idcgList = calIDCG(totRecord,cacmLen)
		for q in queryMatches:

			q 	= q.split(",")
			qId 	= q[0]
			q0 		= q[1]
			docId 	= q[2]
			rank 	= q[3]
			score 	= q[4]

			relevance,relLevel 	= calPrecision(q,cacmMatches,relevance)
			precision 			= relevance/j
			recall 				= relevance/len(cacmMatches)
			dcg					= calDCG(q,dcg,precision,relLevel)
			idcg 				= idcgList[int(rank)-1]
			ndcg 				= dcg/idcg

			s = str(queryNo) + "	" + str(rank) + "	" + str(docId) + "	" + str(score) + "	" +  str(relLevel) + "	" + formatString(precision)  + "	" + formatString(recall) + "	" + formatString(ndcg)
			resultSet.append(s)

			if(relLevel == "1"):
				avg += precision

			if(rank=="20"):
				PatK[i] = precision
			
			# increasing no of records/docs traversed
			j += 1

		AVP[i] = (avg/cacmLen)

		#increasing no of query proccesed
		i += 1

	for a in AVP:
		map += a
	map =  (map/N)
	return map,resultSet,PatK,AVP


def calPrecision(currQuery,cacmMatches,relevance):
	relLevel = "0"

	for m in cacmMatches:
		matchQueId 		= m.split(",")[0]
		matchDocId 		= m.split(",")[2]
		currqueryId 	= currQuery[0]
		currqueryDocId 	= currQuery[2]
		if((matchDocId in currqueryDocId) and (matchQueId in currqueryId)):
			relevance += 1.0
			relLevel = "1"

	return relevance,relLevel


def calDCG(currQuery,dcg,precision,relevanceLevel):
	if relevanceLevel is "1":
	   if currQuery[3] == "1":  #if rank = 1
	       dcg = 1.0
	   else:
	       dcg += 1/math.log(float(currQuery[3]), 2)
	return dcg

	
def calIDCG(totRecord,noOfCacmMatch):
	idcgList = [0]*totRecord
	idcg = 0.0
	for i in range(totRecord):
		rank = i+1
		if(rank<=noOfCacmMatch):
			if rank == 1:  #if rank = 1
				idcg = 1.0
			else:
		   		idcg += 1/math.log(float(rank),2)
		idcgList[i] = idcg
	return idcgList

def formatString(s):
	return str(format(s,'0.6f'))

#--------------------------------------------------------------------------------
#  Function calls
#--------------------------------------------------------------------------------
cacmRes 				= readRelRefFile(refrelFile)
QueryRes 				= readQueryResults(queryResFile)
MAP,resultSet,PatK,AVP 	= processForNQueries(N,maxRecord,QueryRes,cacmRes)

fileName = os.getcwd() + "/" + outputFileName
f = open(fileName,'w')

# printing Average precision value for query
for i in range(len(AVP)):
	s = "Average precision for query " + str(i+1) + " = " + formatString(AVP[i])
	f.write(s + "\n")	

# printing Average precision value for query
f.write("\n")
for i in range(len(PatK)):
	s = "P@K for query " + str(i+1) + " = " + formatString(PatK[i])
	f.write(s + "\n")	

s = "MAP = " + formatString(MAP)
f.write("\n" + s + "\n")	

s = str("Query") + "	" + str("Rank") + "	" + str("Doc Id") + "		" + str("Score") + "		" +  str("Rel Level") + " " + str("Precision")  + "	" + str("Recall") + "		" + str("NDCG")
f.write("\n" + s)	
for i in resultSet:
	f.write( "\n" + i)

f.close()
