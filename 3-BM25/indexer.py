#indexer.py
__author__ = 'Anupma Kushwaha'

from math import log
import collections, os, sys

#--------------------------------------------------------------------------------
#  Setting variables
#--------------------------------------------------------------------------------
corpusDict	= dict()
wordDict 	= dict()
docDict		= dict()
file_path 	= os.getcwd()

#--------------------------------------------------------------------------------
#  Helper functions for inverted index generation
#--------------------------------------------------------------------------------

# Function to create corpus data structure (doc,terms) from input file
def create_corpus(fileName):
	fileName = file_path + '/' + fileName
	f = open(fileName,'r')
	termsInDoc = list()
	for oneLine in f:
		if('#' in oneLine):
			docId = oneLine.split()[1]
		else:
			termsInDoc = oneLine.split()
		add_terms_to_corpusDict(docId,termsInDoc)
	f.close()
	return corpusDict

# Function to add terns to corpus data structure
def add_terms_to_corpusDict(docId,terms):
	if docId in corpusDict:
		for word in terms:
			if not word.isdigit():
				corpusDict[docId].append(word)
	else:
		corpusDict[docId] = []

#Fucntion to create word data structure (term: (doc_id,tf),(doc_id,tf))
def create_word_dictionary(corpus):
	for docId in corpus:
		for word in corpus[docId]:
			if word in wordDict:
				if docId in wordDict[word]:
					wordDict[word][docId] += 1
				else:
					wordDict[word][docId] = 1
			else:
				d 				= dict()
				d[docId] 		= 1
				wordDict[word] 	= d
	return wordDict
	
# Funtion to write inverted index to output file : index.out
def write_index_outputFile(filename,dictionary):
	work_dir = file_path + '/' + filename
	f = open(work_dir,'w')
	f.write(str(dictionary))
	f.close()

#--------------------------------------------------------------------------------
#  For inverted index processing
#--------------------------------------------------------------------------------
def __main__(inputFile,outputFile):
	corpusDict 	= create_corpus(inputFile)
	print('Corpus created!')
	
	wordDict   	= create_word_dictionary(corpusDict)
	print('Word dicitonary created!')
	
	write_index_outputFile(outputFile,wordDict)
	print('Data written to index.out!')

#--------------------------------------------------------------------------------
#  For reading inputs
#--------------------------------------------------------------------------------
inputs 		= sys.argv
input_file 	= sys.argv[1]
output_file = sys.argv[2]
__main__(input_file,output_file)

