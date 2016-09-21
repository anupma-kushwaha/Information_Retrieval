=================================================================================================
Details about assignment
=================================================================================================
	* Assignment is done in python.
	* Python 2.7 is used.
	* Once executed, program will generate a text file of links inside current folder.

=================================================================================================
For executing first part problem:
=================================================================================================
file name       : pageRankPart1.py
input file name : Part1_InputFile.txt
Output file     : Part1_OutputPageRanks.txt

1. Goto location of source code ( pageRankPart1.py file) <location of source code>
2. Execute source code as by giving below command at python idle.
	execfile('<location of file>/pageRankPart1.py')
Ex: My file is placed at C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/
	So I execute as given below
	execfile('C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/pageRankPart1.py')
		or
	python pageRankPart1.py (if present working dir is same as source directory)

3. Once execution is complete, text file of pageranks are generated inside current folder.

=================================================================================================
For executing second part problem:
=================================================================================================
file name       : pageRankPart2.py
input file name : wt2g_inlinks.txt
Output file     : InlinkListTop50.txt, pageRankListTop50.txt, perplexityList.txt

1. Goto location of source code ( pageRankPart2.py file) <location of source code>
2. Execute source code as by giving below command at python idle.
	execfile('<location of file>/pageRankPart2.py')
Ex: My file is places at C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/
	So I execute as given below
	execfile('C:/Users/anuk/anu/WORKSPACES/Python27-WorkSpace/pageRankPart2.py')
		or
	python pageRankPart2.py (if present working dir is same as source directory)

3. Once execution is complete, text file of links is generated inside current folder.



=================================================================================================
ANSWERS to questions asked in Problem statement.
=================================================================================================
1.List of the PageRank values you obtain for each of the six 
  vertices after 1, 10, and 100 iterations of the PageRank algorithm : Part1_InputFile.txt

2.No of all Nodes            : 183811
  No of all inlink lists     : 183811
  No of all outlink lists    : 117636
  No of all sink nodes       : 66175

3. created perplexity list  : perplexityList.txt
4. creating pagerank file   : pageRankListTop50.txt
5. creating inlink file     : InlinkListTop50.txt
6. the proportion of pages with no in-links (sources) = 0.0780693212049
7. the proportion of pages with no out-links (sinks) = 0.360016538727
8. the proportion of pages whose PageRank is less than their initial = 0.00165028727
9. Analysis of the PageRank results:

Web pages with higher number of links pointing to them usually have higher page ranks but it not only depends on who is pointing to web page. Page rank depends on how important a pointing page is, what is the quality of pointing link. 

Ex : X has 20 links pointing to them and Y has 10 links pointing to it. now page rank of X should be higher than page rank of Y but number of links is not only the critiria. It depends on how important pages are which are pointing to X and Y. If very popular page is pointing to Y then Y's page rank will be higher than X. 

Any page has higher page rank value if it has higher number of pages linked to it and pages linked are important and have high page rank of their own.
Pages with higher pag rank usually server better for a given query because their ranks are increased as they have solved the query. This data is fetched form browing history of user or on how long user stays at same page.

Pages with high page ranks can have lower number of links as compared to pages with higher number of links pointing to them. Along with number of links, quality of link also decicde on page rank.


















