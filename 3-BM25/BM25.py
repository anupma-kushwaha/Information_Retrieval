#BM25.py
__author__ = 'Anupma Kushwaha'

from math import log
import collections, os, sys, operator


#--------------------------------------------------------------------------------
#  Setting variables
#--------------------------------------------------------------------------------
k1 = 1.2
k2 = 100
b  = 0.75
R  = 0.0
qf = 1
r  = 0
corpusDict	= dict()
wordDict 	= dict()
docDict		= dict()
queryList	= list()
file_path 	= os.getcwd()

#--------------------------------------------------------------------------------
#  Helper function to read input file and create dta structure to store them
#--------------------------------------------------------------------------------

# Function to create data structure for inverted index (term: (doc_id,tf),(doc_id,tf))
def create_word_dictionary(fileName):
	fileName = file_path + '/' + fileName
	f = open(fileName,'r')
	wordDict = eval(f.read())
	f.close()
	return wordDict

# Function to create data structure corpus (doc:terms)
def create_corpus(wordDictonary):
	for term in wordDictonary:
		docId_tf_list = wordDictonary[term]
		for docId_tf in docId_tf_list:
			docId = docId_tf
			tf = docId_tf_list[docId]
			i = 0
			while(i<tf):
				if docId in corpusDict:
					corpusDict[docId].append(term)
				else:
					corpusDict[docId] = [term]
				i += 1
	return corpusDict

# Function to create document data structure (doc:terms)
def create_doc_dictionary(corpus):
	for docId in corpus:
		size = len(corpus[docId])
		docDict.update({docId: size})
	return docDict

#--------------------------------------------------------------------------------
#  Helper functions for query generation and execution
#--------------------------------------------------------------------------------

# Function to read queries.txt and create structure for storing queries
def query_generator(queryFileName):	
	fileName = file_path + '/' + queryFileName
	with open(fileName) as f:
		lines = ''.join(f.readlines())
	queryList = [x.rstrip().split() for x in lines.split('\n')]
	return queryList

# Function to start calcualting BM25 score for each query
def execute_query(queries,wordDict,docDict):
	resultList 	= list()
	for query in queries:
		x = execute_each_query(query,wordDict,docDict)
		resultList.append(x)
	return resultList

# Function to calcualte BM25 score for each query term
def execute_each_query(queryList,wordDict,docDict):
	query_result = dict()
	N 			 = len(docDict)
	for term in queryList:
		if term in wordDict:
			doc_dict 	= wordDict[term]
			for docId,tf in doc_dict.iteritems():
				n 		= len(doc_dict)
				f 		= tf
				dl 		= getLengthForDocId(docDict,docId)
				avdl 	= getAverageLengthOfDocs(docDict)
				score 	= BM25(n,f,qf,r,N,dl,avdl)
				if docId in query_result:
					query_result[docId] += score
				else:
					query_result[docId] = score
	sorted_results = sorted_query_list(query_result)
	return sorted_results

#--------------------------------------------------------------------------------
#  Helper functioons for BM25 score processing
#--------------------------------------------------------------------------------

# Function to calculate length of each document
def getLengthForDocId(docDict,docId):
	if docId in docDict:
		return docDict[docId]
	else:
		return 0

# Function to calculate average length of documents
def getAverageLengthOfDocs(docDict):
	totalSum = 0
	for length in docDict.itervalues():
		totalSum += length
	result = float(totalSum) / float(len(docDict))
	return result

# Function to calculate BM25 score for a document
def BM25(n, f, qf, r, N, dl, avdl):
	K = k1 * ((1-b) + b * (float(dl)/float(avdl)) )
	part1 	= log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)) )
	part2 	= ((k1 + 1) * f) / (K + f)
	part3 	= ((k2+1) * qf) / (k2 + qf)
	result 	= part1 * part2 * part3
	return result

#--------------------------------------------------------------------------------
#  Helper functions for printing output
#--------------------------------------------------------------------------------	

# Function to sort document list according to BM25 score in reverse order
def sorted_query_list(queryList):
	sortedList = sorted(queryList.items(), key=operator.itemgetter(1),reverse=True)
	return sortedList

# Function to print output to file : results.eval
def print_query_output(queryList,maxResult):
	query_id 	= 1
	Q0 			= "Q0"
	for recordForEachQuery in queryList:
		rank = 1
		for docId_score in recordForEachQuery[:maxResult]:
			docId = docId_score[0]
			BM25_score = docId_score[1]
			# query_id Q0 doc_id rank BM25_score system_name
			string = "query_id = " + str(query_id)
			string = string + ", Q0 = " + Q0
			string = string + ", doc_id = " + str(docId)
			string = string + ", rank = " + str(rank)
			string = string + ", BM25_score = " + str(BM25_score)
			string = string + ", system_name = " + "SystemName123"
			print string 
			rank += 1
		query_id += 1

#--------------------------------------------------------------------------------
#  To start processing for calcualting BM25 score for query and documents
#--------------------------------------------------------------------------------
def __main__(inputFile,queryFile,maxResult):
	
	wordDict 	= create_word_dictionary(inputFile)
	
	corpusDict 	= create_corpus(wordDict)
	
	docDict   	= create_doc_dictionary(corpusDict)

	queryList 	= query_generator(queryFile)
	
	queryList 	= execute_query(queryList,wordDict,docDict)

	print_query_output(queryList,maxResult)

#--------------------------------------------------------------------------------
#  For reading inputs
#--------------------------------------------------------------------------------
index_file 	= sys.argv[1]
query_file  = sys.argv[2]
max_result 	= int(sys.argv[3])
__main__(index_file,query_file,max_result)

