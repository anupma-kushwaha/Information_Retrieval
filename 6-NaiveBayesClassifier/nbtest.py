__author__ = 'Anupma Kushwaha'

import collections, os, sys, operator, glob, math
from collections import OrderedDict

#--------------------------------------------------------------------------------
#  Setting variables
#--------------------------------------------------------------------------------
working_dir 	= os.getcwd()

#--------------------------------------------------------------------------------
#  Functions
#--------------------------------------------------------------------------------
def read_model_files(fileName):

	modelFileName = working_dir + "/" + fileName

	f = open(modelFileName,'r')
	text = ''.join(f.readlines())
	dict1, dict2 = text.split("\n")
	trainPosDict = eval(dict1)
	trainNegDict = eval(dict2)
	f.close()
	return trainPosDict,trainNegDict

def read_test_files(testFileName):

	testFileName = working_dir + "/" + testFileName
	
	testDocList 		= list()
	testFilenameList	= list()
	
	for testFileName in glob.glob(os.path.join(testFileName, '*.txt')):
		testFilenameList.append(testFileName)
		with open(testFileName) as f:
		    text 		= ''.join(f.readlines())
		    oneDocList 	= []
		    for i in text.split('\n'):
		        term = i.rstrip().split()
		        oneDocList.extend(term)
		testDocList.append(oneDocList)

	return testDocList,testFilenameList

def calculate_probability(docList,probDictionary):
	probrability_list = list()

	for doc in docList:
		p = 0.0
		for term in doc:
			if term in probDictionary:
				p += math.log(probDictionary[term])
		probrability_list.append(p)
	return probrability_list

def calculateCounts(outputFile,posProb,negProb):
	i = 0
	negRecordCount = 0
	posRecordCount = 0

	while i < len(posProb):
		if posProb[i] <= negProb[i]:
			negRecordCount += 1
		else:
			posRecordCount += 1
		i += 1

	print("negative count: " + str(negRecordCount) + ", positive count: " + str(posRecordCount))

	filepath = working_dir + "/" + outputFile
	string1 = "positive count for test files: " + str(posRecordCount)
	string2 = "negative count for test files: " + str(negRecordCount)
	with open(filepath, 'a') as f:
		f.write(string1 + "\n")
		f.write(string2 + "\n \n")
 	f.close()

	return posRecordCount,negRecordCount

def top20LogRatios(posProb,negProb):
	posToNegRatio = {}
	negToPosRatio = {}
	for i in posProb.keys():
		posToNegRatio[i] = math.log(posProb[i]) - math.log(negProb[i])
		negToPosRatio[i] = math.log(negProb[i]) - math.log(posProb[i])

	top20PosToNegRatio = sorted(posToNegRatio.items(), key=operator.itemgetter(1), reverse = True)[:20]
	top20NegToPosRatio = sorted(negToPosRatio.items(), key=operator.itemgetter(1), reverse =True)[:20]

	return top20PosToNegRatio,top20NegToPosRatio

def writeProbabilityForEachTestFile(outputFile,fileNameList,posProb,negProb):
	filepath = working_dir + "/" + outputFile
	with open(filepath, 'a') as f:
		j = 0
		s = "Predictions for test files"
		f.write(s + "\n")
		s =  "No. 	Filename 	Pos Probability 	Neg Probability"
		f.write(s + "\n \n")
		while j < len(fileNameList):
			s = str((j+1)) + " 	" + fileNameList[j].split('\\')[-1:][0]  + " 	" +  str(posProb[j])  + " 		" +  str(negProb[j])
			f.write(s + "\n")
			j += 1
	f.close()
	
def writeIntoFile(fileName,listOfProb, string):
	filepath = working_dir + "/" + fileName
	with open(filepath, 'a') as f:
		f.write(string + "\n")
		for i in listOfProb:
			f.write(str(i) + "\n")
		f.write("\n")
 	f.close()

#--------------------------------------------------------------------------------
#  Function calls
#--------------------------------------------------------------------------------
def __main__(modelFile,testFile,outputFile):
	
	trainPosDict,trainNegDict		= read_model_files(modelFile)
	testDocList,testFilenameList	= read_test_files(testFile)

	testPosProb = calculate_probability(testDocList,trainPosDict)
	testNegProb = calculate_probability(testDocList,trainNegDict)
	posRecordCount,negRecordCount  = calculateCounts(outputFile,testPosProb,testNegProb)
	
	top20PosToNegRatio,top20NegToPosRatio = top20LogRatios(trainPosDict,trainNegDict)
	writeIntoFile(outputFile,top20PosToNegRatio,"Top 20 Positive to Negative Ratios \n")
	writeIntoFile(outputFile,top20NegToPosRatio,"Top 20 Negative to Positive Ratios \n")

	writeProbabilityForEachTestFile(outputFile,testFilenameList,testPosProb,testNegProb)

#--------------------------------------------------------------------------------
#  For reading inputs
#--------------------------------------------------------------------------------
# nbtest <model-file> <test-directory> <predictions-file>
# python nbtest.py model.txt /textcat/test prediction.txt

model_file  	= sys.argv[1]
test_file  		= sys.argv[2]
output_file		= sys.argv[3]

__main__(model_file,test_file,output_file)

