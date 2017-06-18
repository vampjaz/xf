from bs4 import BeautifulSoup
import requests
import time
from urlparse import urlparse

desc = 'crawls a website from a given starting point and lists the URLs found'
author = 'nwx'
cmds = []

def localcrawl():
	global visited
	visited = []
	host = raw_input('URL to start crawling? ')
	recursion = input('number of recursion levels? ')
	crawl(host,recursion,delay=1,extern=False)
cmds.append(('spider','crawls a website, following local links only, and lists URLs',localcrawl))

def globalcrawl():
	global visited
	visited = []
	host = raw_input('URL to start crawling? ')
	recursion = input('number of recursion levels? ')
	crawl(host,recursion,delay=1,extern=True)
cmds.append(('gspider','crawls a website, following all links, and lists URLs',globalcrawl))

visited = []

def crawl(host,recursion,delay=2,extern=False,indent=0):
	global visited
	timer = time.time()
	try:
		req = requests.get(host)
		visited.append(host)
	except (requests.exceptions.MissingSchema,requests.exceptions.ConnectionError) as e:
		print '{} {} - {}'.format(' '*indent,host,e)
		return
	print '{} {} - {} ({} ms)'.format(' '*indent,host,req.status_code,int((time.time()-timer)*1000))
	time.sleep(delay)
	if recursion >= 0 and req.status_code == 200:
		soup = BeautifulSoup(req.text, 'html.parser')
		parsed_uri = urlparse(host)
		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri) # used for resolving relative links
		if domain.endswith('/'):
			folder = domain
		else:
			folder = domain.rsplit('/',1)[0]
		links = soup.find_all('a')
		for l in links:
			u = l.get('href')
			if not u or u.startswith('#'):
				continue # don't follow these
			candidate_uri = urlparse(u)
			if not extern and candidate_uri.netloc and candidate_uri.netloc != parsed_uri.netloc:
				continue
			if not candidate_uri.netloc:
				if u.startswith('/') or u.startswith('.'):
					u = domain + u
				else:
					u = folder + u
			if u in visited:
				return
			crawl(u,recursion - 1,delay=delay,extern=extern,indent=indent+1)
