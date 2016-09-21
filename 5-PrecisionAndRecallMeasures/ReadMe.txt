=================================================================================================
Details about assignment
=================================================================================================
	* Assignment is coded in Python 2.7
	* Once executed, program will generate output file inside current folder

=================================================================================================
For executing program:
=================================================================================================
file name       : retrivalEff.py
Input file name	: Query.txt, cacm.rel.txt
Output file     : results.txt

1. Open command prompt

2. Goto location of source code (retrivalEff.py file)
	Eg : C:\Users\anuk\Desktop\hm5\

3. Execute source code by giving below command at command prompt
	python retrivalEff.py

4. Program results will be generated and stored inside current folder path with name results.txt file
	Eq : C:\Users\anuk\Desktop\hm5\results.txt

=================================================================================================
Query mapping
=================================================================================================
portable operating systems (12)			: Query 1
code optimization for space efficiency (13)	: Query 2
parallel algorithms (19)			: Query 3

Above(12,13,19) three queries are refered in result.txt as 1,2,3 respectively

=================================================================================================
Questions asked in problem statement
=================================================================================================
1. ReadMe.txt
	: included by same name

2. Your source code to evaluate retrieval effectiveness
	: included sources code by name retrivalEff.py

3. Calcualted below 5 measures for each query 12,13 and 19.
	1- Precision
	2- Recall
	3- P@K, where K = 20
	4- Normalized Discounted Cumulative Gain (NDCG)
	5- Mean Average Precision (MAP)

	: All 5 values are calculated for each query and each
	  document and stored in results.txt

4. Included one table for each query, in total 3 tables with below columns
	Rank
	Document ID
	Document score
	Relevance level
	Precision
	Recall
	NDCG

	: All 7 values are calculated for each query and each
	  document and stored in results.txt

5. Included 3 values of P@20, one for each query
	: These are sotred at the top of results.txt file
	  Below are the values
		P@K for query 1 = 0.150000
		P@K for query 2 = 0.250000
		P@K for query 3 = 0.450000
		
		Average precision for query 1 = 0.479545
		Average precision for query 2 = 0.198600
		Average precision for query 3 = 0.565880

6. Included 1 value for MAP
	: This is sotred at the top of results.txt file
	  Below is the value
	  
	  MAP = 0.414675
