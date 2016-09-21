=================================================================================================
Details about assignment
=================================================================================================
	* Assignment is coded in python 2.7.
	* Once executed, program will generate all output files inside current folder.

=================================================================================================
For executing first part of problem (Indexer):
=================================================================================================
file name       : indexer.py
input file name : tccorpus.txt
Output file     : index.out

1. Goto location of source code ( indexer.py file)
2. Execute source code by giving below command at command prompt
	python indexer.py tccorpus.txt index.out

3. Once execution is complete, inverted index file (index.out) will be generated inside 
   current folder.

=================================================================================================
For executing second part problem (BM25 Ranking algorithm):
=================================================================================================
file name       : BM25.py
input file name : index.out,queries.txt
Output file     : results.eval

1. Goto location of source code (BM25.py file)
2. Execute source code by giving below command at command prompt
	python BM25.py index.out queries.txt 100 > results.eval

3. Once execution is complete, result file will be generated inside current folder.

=================================================================================================
Approach for solving problem
=================================================================================================
indexer.py
Processing start by calling "main function"
indexer.py generate inverted index, corpus is read for each document at a time and word dictionary is created.
Word dictionary will store word/term as key and value will be (document id and term frequency)
Word dicitonary is inverted index, which is written in index.out file


BM25.py
Processing start by calling "main function"
To calculate score, index.out is read which is generated from first part and word dictionary is reconstrcuted from file.
Corpus and document dictionary is created from word dictionary
Document dictionary has document id as key and all terms as value
Query generator will read queries.txt and create query term list
Query list and word dictionary is send to execute query function which generates BM score.
Query Execution function is executed for each query and each query term on all documents in corpus
Query results is a dicitonary with document id as key and BM25 score as value.
This is sorted in reverse order of BM25 score
Finally top 100 results for each query are written to results.eval

