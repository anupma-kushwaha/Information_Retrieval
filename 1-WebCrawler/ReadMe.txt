Details about assignment

	* Assignment is done in python.
	* Python 2.7 is used.
	* BeautifulSoup library is used for crawling. (bs4)
	* Once executed, program will generate a text file of urls at C:\Python27 or file where ever python is located.

Total Pages retrieved by focused crawling are 20000
Total Pages retrieved by focused crawling with keyword ‘concordance’are 176

Naming convention for output files generated
	File with no keywords 	: crawled-urls-noKeyword.txt
	File with with keywords : crawled-urls-withKeyword.txt

Library bs4 is included in folder being submitted. This has to be in placed inside C:\Python27\Lib\

Instructions to execute source code:

1. Make sure beautifulSoup library is available inside Python/Lib folder (C:\Python27\Lib\bs4)
2. Get location of source code ( spider.py file) <location of source code>
3. Execute source code as by giving below command at python idle.
	execfile('<location of file>/spider.py')
Ex: My file is places at C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/
	So I execute as given below
	execfile('C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/spider.py')
4. Once execution is complete, text file of urls is generated inside Python folder. (C:\Python27) 
	– I choose this path to generate output file because it can be easily located.

