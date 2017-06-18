import hashlib
from libs.zippycrack import *

desc = 'provides hashing and brute-force hash cracking'
author = 'nwx'
cmds = []

def hashstring():
	inp = raw_input('string to hash> ')
	algos = {}
	for i in hashlib.algorithms_available:
		algos[i] = hashlib.new(i)
	for i in algos.keys():
		algos[i].update(inp)
	for i in algos.keys():
		print '{} :\t{}'.format(i,algos[i].hexdigest())
cmds.append(('hash','hash a string with several different algorithms',hashstring))

def hashfile():
	fn = raw_input('file path> ').strip()
	algos = {}
	for i in hashlib.algorithms_available:
		algos[i] = hashlib.new(i)
	fd = open(fn,'rb')
	while 1:
		indata = fd.read(8192)
		for i in algos.keys():
			algos[i].update(indata)
		if len(indata) < 8192:
			break
	for i in algos.keys():
		print '{} :\t{}'.format(i,algos[i].hexdigest())
cmds.append(('hashfile','hash a file with several different algorithms',hashfile))

def bruteforce():
	out = raw_input('hash to crack> ')
	print 'algorithms supported: '+', '.join(hashlib.algorithms_available)
	algo = raw_input('algorithm to use> ')
	if not algo in hashlib.algorithms_available:
		print 'invalid algorithm'
		return
	fn = raw_input('path to password list> ').strip()
	def check(pw):
		h = hashlib.new(algo)
		h.update(pw)
		if h.hexdigest() == out:
			return True
		return False
	zc = zippycrack(check,fn,numthreads=8)
	print zc.run()
cmds.append(('hashcrack','brute forces a hash using multiple threads and algorithms',bruteforce))
