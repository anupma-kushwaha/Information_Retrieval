=================================================================================================
Details about assignment
=================================================================================================
	* Assignment is coded in Java using Eclipse Mars.
	* Once executed, program will generate all output files inside folder given as index folder.

=================================================================================================
For executing program:
=================================================================================================
file name       : LuceneSearchEngine.jar, corpus
Output file     : termFreq.txt, QueryResults.txt

1. Open command prompt
2. Goto location of source code (LuceneSearchEngine.jar file)
	Eg : C:\Users\anuk\Desktop\Lucene\

3. Execute source code by giving below command at command prompt
	java -jar LuceneSearchEngine.jar

4. Once execution is started, program will ask for path of index folder.
	Eg : C:\Users\anuk\Desktop\Lucene\

5. Next program will ask for corpus folder path. 
	Eg : C:\Users\anuk\Desktop\Lucene\corpus

6. Next program will ask for query to be searched.
	Eg : portable system

7. Query results will be generated and stored at index folder path with name QueryResults.txt file

8. Term frequency results will be generated and stored at index folder path with name termFreq.txt file

=================================================================================================
Things to note before execution
=================================================================================================
Please clear index folder incase you are executing for second or more times.

=================================================================================================
Questions asked in problem statement
=================================================================================================
1. ReadMe.txt
	: included by same name

2. Your source code for indexing and retrieval 
	: included runnable jar LuceneSearchEngine.jar for execution
	: included folder LuceneSearchEngine from eclipse workspace containing all sources

3. A sorted (by frequency) list of (term, term_freq pairs) 
	: included termFreq.txt file inside my_results folder

4. A plot of the resulting Zipfian curve
	: included zipfCurve.jpg image and excel plot.xlsx which has all x-y values

5A. Four lists (one per query) each containing at MOST 100 docIDs ranked by score
	: included four (QueryResults-x.txt) files inside my_results folder

5B. Optional: provide a text snippet of 200 chars along the DocID
	: Included text snippet for each document which is hit for query.
	  Text snippets are stored in QueryResults-x.txt files along with score
	  and docId inside my_results folder

6. A table comparing the total number of documents retrieved per query using Lucene’s 
   scoring function vs. using your search engine (index with BM25) from the previous assignment

	Total document hits for 4 queries using BM25 in hw3 and Lucene in hw4

	Sl No	Query						BM25	Lucene
	-----------------------------------------------------------------------
	1	portable operating systems			871	440
	2	code optimization for space efficiency		1632	1579
	3	parallel algorithms				1386	272
	4	parallel processor in information retrieval	1540	1529

	Same table is stored in second tab of plot.xlsx excel




