package com.ir.src;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Fields;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.MultiFields;
import org.apache.lucene.index.Term;
import org.apache.lucene.index.Terms;
import org.apache.lucene.index.TermsEnum;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.BytesRef;

public class customFunctions {
	/**
	 * Calculate term frequency
	 * @param reader the Indexer Reader and index is path of index file
	 * @throws java.io.IOException when exception creating term frequency.
	 */
	public static void termFreqGenerator(IndexReader reader, String index) throws IOException{
		try {
			// Calculating term frequency
			HashMap<String, Long> termFreqHash = new  HashMap<String, Long>();
			reader = DirectoryReader.open(FSDirectory.open(new File(index)));
			Fields fields = MultiFields.getFields(reader);
			Terms terms = fields.terms("contents");
			TermsEnum iterator = terms.iterator(null);
			
			BytesRef byteRef = null;
			while((byteRef = iterator.next()) != null) {
				String term = new String(byteRef.bytes, byteRef.offset, byteRef.length);
				Term termInstance = new Term("contents", term);                              
				long termFreq = reader.totalTermFreq(termInstance);
				termFreqHash.put(term, termFreq);
			}
			System.out.println("total number of terms = " + termFreqHash.size());
			
			//sorting term frequency in reverse order
			TreeMap<String, Long> sortedTermFreq = sortByValue(termFreqHash);
			
			//writing term frequency to file
			writeIndexFile(index,sortedTermFreq);
		}
		catch (IOException e) {
			System.out.println("exception caught while calculating term frequency " + e);
		}
	}

	/**
	 * Sort term frequency in descending order
	 * @param hashmap of term and its frequency
	 */
	private static TreeMap<String, Long> sortByValue(HashMap<String, Long> map) {
		ValueComparator vc =  new ValueComparator(map);
		TreeMap<String,Long> sortedMap = new TreeMap<String,Long>(vc);
		sortedMap.putAll(map);
		return sortedMap;
	}
	
	/**
	 * Write term frequency into text file
	 * @param path of index file and Treemap of term and frequency
	 * @throws java.io.IOException when exception when sorting term frequency.
	 */
	private static void writeIndexFile(String index, TreeMap<String, Long> sortedTermFreq)throws IOException{
		String fileName = index + "/termFreq.txt";
		PrintWriter printWriter;
		try {
			printWriter = new PrintWriter(new FileWriter(new File(new String(fileName))));
			for(Map.Entry<String,Long> entry : sortedTermFreq.entrySet()) {
				  String term = entry.getKey();
				  Long termFreq = entry.getValue();
				  printWriter.write(term + " : " + termFreq + "\n");
				}		
			printWriter.close();
		} catch (IOException e) {
			System.out.println("exception caught while storing term frequency " + e);
		}
	}

	/**
	 * Removed html and pre tags from content of file
	 * @param File whose contents has to be parsed and tags has t be removed
	 * @throws java.io.IOException when exception while removing html tags
	 */
	public static FileReader removeUnwantedTags(File file) throws IOException{
		FileReader fr = null;
		try {
			fr = new FileReader(file);
			PrintWriter printWriter = new PrintWriter(new FileWriter(new File(new String("noHtmlTag.txt"))));
			BufferedReader bufferedReader = new BufferedReader(fr);

			String line;
			while((line = bufferedReader.readLine()) != null) {
				String s = line.replaceAll("\\<[^>]*>",""); //replaceAll("<pre>","");
				printWriter.write(s + "\n");
			}       
			fr.close();        
			bufferedReader.close(); 
			printWriter.close();
			fr = new FileReader("noHtmlTag.txt");
		} catch (FileNotFoundException e) {
			System.out.println("exception caught while removing html tags " + e);
		}
		return fr;
	}
	
	/**
	 * Write query hit results into txt file
	 * @param given query, list of searched documents with query terms,
	 *        path of index file, index searcher and size of result set   
	 * @throws java.io.IOException when exception creating term frequency.
	 */
	static void writeQueryResultFile(String query, ScoreDoc[] hits,
			String indexLocation, IndexSearcher searcher, int resultSet) throws IOException{
		
		String fileName = indexLocation + "/QueryResults.txt";
		PrintWriter printWriter;
		try {
			printWriter = new PrintWriter(new FileWriter(new File(new String(fileName))));
			printWriter.write("QUERY : " + query + "\n");
			printWriter.write("Total number of matches : " + hits.length + "\n");
			int x = (resultSet<hits.length) ? resultSet : hits.length;
			for (int i = 0; i < x ; ++i) {
				int docId = hits[i].doc;
				Document d = searcher.doc(docId);
				String id = d.get("path").substring(d.get("path").length() -14,d.get("path").length() - 5);
				String snippet = snippet(d.get("path"));
				printWriter.write(i+1 + " : docId = " + id + " , score = " + hits[i].score + " , Text Snippet = "+ snippet + "\n");
			}		
			printWriter.close();
		} catch (IOException e) {
			System.out.println("exception caught while storing query results " + e);
		}
	}
	
	/**
	 * Fetch text snippet
	 * @param path of index file   
	 * @throws java.io.IOException when exception while fetching text snippet.
	 */
	private static String snippet(String path){
		FileReader fr = null;
		String s = "";
		try {
			fr = new FileReader(path);
			BufferedReader bufferedReader = new BufferedReader(fr);
			String line;
			while((line = bufferedReader.readLine()) != null) {
				s = s + line.replaceAll("\\<[^>]*>","");
			}   
			if(s.length() > 200) s = s.substring(0,200);
			fr.close();	
			bufferedReader.close(); 
		}
		catch (IOException e) {
			System.out.println("exception caught while creating text snippet " + e);
		}
		return s;
	}
}

/**
 * Class which implements Comparator interface 
 * to sort term frequency in descending order. 
 */
class ValueComparator implements Comparator<String> {	 
	HashMap<String, Long> map;
    public ValueComparator(HashMap<String, Long> base) {
        this.map = base;
    }

    /**
     * Implements compare function of comparator interface 
     * @param two input strings
     */
    public int compare(String a, String b) {
        if (map.get(a) >= map.get(b)) {
            return -1;
        } else {
            return 1;
        }
    }
}

