from libs.ip import *
import whois  # pip intall pywhois

desc = 'looks up a website whois information'
author = 'nwx'
cmds = []

def lookup():
	host = raw_input('website (without protocols like HTTP or any slashes)> ')
	w = whois.whois(host)
	print w
cmds.append(('whois','looks up a website\'s whois info',lookup))
