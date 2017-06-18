## something strange i've found: zipfiles sometimes can be decrypted by multiple different passwords
## uses my library zippycrack which is included

import zipfile, sys, os
from libs.zippycrack import *

desc = 'multi-threaded zipfile password bruteforcer'
author = 'nwx'
cmds = []



def zipcracker():
	filename = raw_input('zip file> ').strip()
	pwlist = raw_input('password list file> ').strip()
	if not os.path.exists(filename):
		print "error: zip file {} doesn't exist".format(filename)
		return
	if not os.path.exists(pwlist):
		print "error: password list file {} doesn't exist".format(pwlist)
		return
	def try_deflate(password):
		try:
			zfile = zipfile.ZipFile(filename)
			zfile.extractall(pwd=password)
			return True
		except:
			return False
	zc = zippycrack(try_deflate,pwlist,numthreads=8,cont=True)
	zc.run()
cmds.append(('zipcrack','brute forces a password protected zip file using a wordlist',zipcracker))
