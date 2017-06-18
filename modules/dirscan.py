import requests
import time, os

desc = 'scans a website for different directories of interest using brute-force and a list of dirs'
author = 'nwx'
cmds = []
# use something like https://github.com/danielmiessler/RobotsDisallowed

def scansite():
	site = raw_input('website url> ').rstrip('/')
	lst = raw_input('path to uri list> ').strip()
	delay = input('time to delay in between requests? ')
	fd = open(lst,'r')
	for d in fd.readlines():
		url = site + d
		r = requests.get(url)
		if r.response_code in [200,301,302,303]:
			print url,' - ',r.response_code
		time.sleep(delay)
