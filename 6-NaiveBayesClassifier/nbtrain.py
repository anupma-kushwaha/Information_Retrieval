__author__ = 'Anupma Kushwaha'

import collections, os, sys, operator
from collections import OrderedDict

#--------------------------------------------------------------------------------
#  Setting variables
#--------------------------------------------------------------------------------
outputFileName 	= "output.txt"
working_dir 	= os.getcwd()
trainPosDict 	= dict()
trainNegDict 	= dict()

#--------------------------------------------------------------------------------
#  Functions
#--------------------------------------------------------------------------------
def read_input_files(fileName):

	trainFileName  	= working_dir + "/" + fileName

	trainPosFileName = trainFileName + "/pos/" 
	trainNegFileName = trainFileName + "/neg/"

	trainPosDict 	= readTextFiles(trainPosFileName)
	trainNegDict 	= readTextFiles(trainNegFileName)

	return trainPosDict,trainNegDict

def readTextFiles(fileName):
	train_dict 	= dict()
	wordList	= list()

	for dir_entry in os.listdir(fileName):
		file_entry_path = os.path.join(fileName, dir_entry)
		if os.path.isfile(file_entry_path):
			with open(file_entry_path, 'r') as one_file:
				file_data = one_file.read()
				wordList = [x.rstrip().split() for x in file_data.split("\n")]
				combinedWordList = [item for sublist in wordList for item in sublist]
				for one_word in combinedWordList:
					if one_word in train_dict:
						train_dict[one_word] = train_dict[one_word] + 1
					else:
						train_dict[one_word] = 1

	return sort_dictionary(train_dict)

def sort_dictionary(dictionary):
	sortedList = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))
	return sortedList

def equate_dictionary(dictionary1,dictionary2):
    for k,v in dictionary1.iteritems():
        if k not in dictionary2:
            dictionary2[k] = 0
    return dictionary2

def remove_records_less_than_five_freq(posDictionary,negDictionary):
	for k in posDictionary.keys():
		if posDictionary[k] + negDictionary[k] < 5:
			del posDictionary[k]
			del negDictionary[k]
	return posDictionary, negDictionary

def calculate_probability(dictionary):
	probrability_dict = dict()
	vocab_len 	= len(dictionary)
	count 		= sum(dictionary.values())
	for k,v in dictionary.items():
		p = (float(v) + 1)/(count + vocab_len)
		probrability_dict[k] = p
	return probrability_dict

def writeIntoFile(fileName,posProbDict,negProbDict):
	filepath = working_dir + "/" + fileName
	f = open(filepath, 'w')
	f.write(str(posProbDict))
	f.write("\n")
	f.write(str(negProbDict))
	f.close()
#--------------------------------------------------------------------------------
#  Function calls
#--------------------------------------------------------------------------------
def __main__(inputFile,outputFile):
	
	trainPosDict,trainNegDict = read_input_files(inputFile)

	trainNegDict = equate_dictionary(trainPosDict,trainNegDict)
	trainPosDict = equate_dictionary(trainNegDict,trainPosDict)

	trainPosDict,trainNegDict = remove_records_less_than_five_freq(trainPosDict,trainNegDict)

	trainPosProb = calculate_probability(trainPosDict)
	trainNegProb = calculate_probability(trainNegDict)

	s = "total training terms  : " + str(len(trainPosDict))
	print s

	writeIntoFile(outputFile,trainPosProb,trainNegProb)

#--------------------------------------------------------------------------------
#  For reading inputs
#--------------------------------------------------------------------------------
# nbtrain <training-directory> <model-file>
# python nbtrain.py /textcat/train model.txt >>output.txt

train_file  	= sys.argv[1]
model_file  	= sys.argv[2]

__main__(train_file,model_file)
