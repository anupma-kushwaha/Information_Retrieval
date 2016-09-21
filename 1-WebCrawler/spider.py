import urlparse
import urllib	
from bs4 import BeautifulSoup
import time
import os


#---------------------------------------------------------------------#
#Global variables
#---------------------------------------------------------------------#
seed=raw_input('Enter a url : ')
keyword=raw_input('Enter a keyword : ')
max_link = 10
max_depth = 5
crawl_depth = 1
top_url = 'http://en.wikipedia.org'

if len(keyword)==0:
	work_dir = os.getcwd() + '/crawled-urls-noKeyword.txt'
else:
	work_dir = os.getcwd() + '/crawled-urls-withKeyword.txt'
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
#crawl : function to crawl all relevant links on web
#---------------------------------------------------------------------#
def crawl(seed,keyword):

	global crawl_depth
	global to_crawl
	global crawled
	global max_link
	global max_depth

	to_crawl = [seed]  		# list of to_crawl, urls to be visited
	depth_to_crawl = [1]  	# list of depths for to_crawl urls
	crawled  = [] 			# urls already visited

	while len(to_crawl) > 0 and len(crawled) <= max_link and max(depth_to_crawl) <= max_depth:
		try:
			htmlText = urllib.urlopen(to_crawl[0]).read()
			time.sleep(1)
		except:
			break

		getLinksInAPage(to_crawl[0],htmlText,keyword,depth_to_crawl)

	crawl_depth = max(depth_to_crawl)
	return sorted(crawled)
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
# getLinksInAPage : Function to get aal links on a given page
#---------------------------------------------------------------------#
def getLinksInAPage(seed,htmlUrl,keyword,depth_to_crawl):
	
	global to_crawl
	global crawled
	global max_link
	global top_url

	soup = BeautifulSoup(htmlUrl)

	if len(keyword)==0 and seed not in crawled:
		crawled.append(seed)
	else:
		body = soup.body.text
		body = body.encode('utf-8')
		if  keyword.lower() in body.lower() and seed not in crawled:
			crawled.append(seed)

	to_crawl.pop(0)
	current_level = depth_to_crawl.pop(0)
	
	for tag in soup.find_all('a',href=True):

		hrefTag = tag['href'].encode('utf-8')
		if hrefTag.find('.wikipedia.org') or hrefTag.find('/wiki/'):
		
			if hrefTag.find('.wikipedia.org') >= 0:
				index = hrefTag.find('.wikipedia.org')
				lang = hrefTag[index-2:index]
		
				if 'en' not in lang:
					continue
				
			if '#' in hrefTag or '?' in hrefTag or '.' in hrefTag or \
			':' in hrefTag or '/wiki/Main_Page' in hrefTag:
				continue
			else:
				hrefTag = top_url + hrefTag
				if hrefTag not in crawled and len(crawled) <= max_link:
					to_crawl.append(hrefTag)
					depth_to_crawl.append(current_level + 1)
		else:
			continue
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
# write_url_to_file : funciton to write output urls in output text file
#---------------------------------------------------------------------#
def write_url_to_file(list_of_urls):

	global work_dir
	if list_of_urls > 0:
		
		f = open(work_dir,'w')
		for one_url in list_of_urls:
			f.write(one_url + '\n')
		f.close()	
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
#Function call to crawl to find all relavant links on web
#---------------------------------------------------------------------#
crawled_list = crawl(seed,keyword)
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
# Function call to write_url_to_file to write all urls in output text file
#---------------------------------------------------------------------#
write_url_to_file(crawled_list)
#---------------------------------------------------------------------#

