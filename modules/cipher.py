#### cipher guessing program

desc = 'guesses a few simple text ciphers using brute force and word counting, also allows you to encode/decode directly'
author = 'nwx'
cmds = []

import string, itertools, os, base64

def rotate(txt,n):
	return txt[n:] + txt[:n]

def score(txt):
	sc = 0
	txt = txt.lower()
	fd = open(os.path.join(os.path.dirname(__file__),'data/wordlist.txt'))
	for i in fd.readlines():
		i = i.strip().lower()
		if i in txt:
			sc += len(i)
	fd.close()
	return sc

############################################################# individual ciphers
ciphers = []

def caesar(txt,key):
	out = [l + '_' for l in txt]
	for o,r in zip(string.ascii_lowercase,rotate(string.ascii_lowercase,key)) + zip(string.ascii_uppercase,rotate(string.ascii_uppercase,key)):
		for i,l in zip(range(len(txt)),out):
			if l[0] == o and len(l) > 1 and l[1] == '_':
				out[i] = r
	return ''.join([l[0] for l in out])

def caesar_guess(txt):
	for i in range(26):
		yield 'caesar {}'.format(i), caesar(txt,i)

ciphers.append(caesar_guess)
###########################################

def atbash(txt):
	out = [l + '_' for l in txt]
	for o,r in zip(string.ascii_lowercase,reversed(string.ascii_lowercase)) + zip(string.ascii_uppercase,reversed(string.ascii_uppercase)):
		for i,l in zip(range(len(txt)),out):
			if l[0] == o and len(l) > 1 and l[1] == '_':
				out[i] = r
	return ''.join([l[0] for l in out])

def atbash_guess(txt):
	yield 'atbash',atbash(txt)

ciphers.append(atbash_guess)
###########################################

def base64_decode(txt):
	try:
		return base64.b64decode(txt)
	except:
		return ''

def base64_guess(txt):
	yield 'base64',base64_decode(txt)

ciphers.append(base64_guess)
###########################################



############################################################# guessing stuff

def guess_cipher(txt):
	answers = []
	for a in ciphers:
		for b in a(txt):
			answers.append(b)
	scores = []
	for a in answers:
		scores.append((a[0],score(a[1]),a[1]))
	scores.sort(key=lambda a:a[1])
	return scores[-1][0],scores[-1][2]

def decipher():
	ct = raw_input('enter cipher text: ')
	print guess_cipher(ct)
cmds.append(('cipher','brute force simple ciphers and finds the answer with the most recognizable words',decipher))
