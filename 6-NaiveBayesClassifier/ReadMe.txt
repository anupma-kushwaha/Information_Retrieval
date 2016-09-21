=================================================================================================
Details about assignment
=================================================================================================
	* Assignment is coded in Python 2.7
	* Once executed, program will generate output file inside current folder

	Submitted by : Anupma Kushwaha and Roop Kumar Ghosh.

=================================================================================================
For executing program:
=================================================================================================
file name       : nbtrain.py, nbtest.py
Input directory	: textcat
Output file     : output.txt,model.txt,prediction.txt (or whatever name given by user)

1. Open command prompt

2. Goto location of source code (nbtrain.py file)
	Eg : C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine

3. Execute source code by giving below command at command prompt
	python nbtrain.py <training-directory> <model-file>
	Eg : python nbtrain.py /textcat/train model.txt >> output.txt

4. Program results will be generated and stored inside current folder path with name 
   outpuut.txt and model.txt file
	Eq : C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine\model.txt
	     C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine\output.txt

5. Goto location of source code (nbtest.py file)
	Eg : C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine

6. Execute source code by giving below command at command prompt
	python nbtest.py <model-file> <test-directory> <predictions-file>
	Eg : python nbtest.py model_Anu.txt /textcat/test prediction.txt

7. Program results will be generated and stored inside current folder path with name prediction.txt file
	Eq : C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine\prediction.txt


=================================================================================================
Regarding file path for textcat 
=================================================================================================
Please mention path of file from current folder.

Eg :	Current folder : 
	C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine
	
	File path for test which is inside folder textcat/test which is inside current folder.
	
	Test folder -
	C:\Users\anuk\anu\NEU_Study\FALL-2015\IR-Nada\Assignment\6\mine\textcat\test

=================================================================================================
Questions asked in problem statement
=================================================================================================
1. ReadMe.txt
	: included by same name

2. Your source code to build naive bayes classifier
	: included sources code by name nbtrain.py and nbtest.py

3. predictions file for the development data
	: This is stored in predictionDevNeg.txt and predictionDevPos.txt file
	: For Positive development data
		positive count for dev files: 75
		negative count for dev files: 25
		Correctly marked  = 75%
	
	: For Negative development data
		positive count for test files: 20
		negative count for test files: 80
		Correctly marked  = 80%

4. predictions file for the test data
	: This is stored in prediction.txt file

5. A list of the 20 terms with the highest (log) ratio of 
   positive to negative weight.
	: This is stored at the top of prediction.txt file

6. A list of the 20 terms with the highest (log) ratio of 
   negative to positive weight.
	: This is stored at the top of prediction.txt file

