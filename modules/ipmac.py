import socket, os, sqlite3
from libs.ip import *

desc = 'assists with calculating IPv4 and MAC address info'
author = 'nwx'
cmds = []

dbfile = os.path.join(os.path.dirname(__file__),'data/nmap.db')

def maclookup():
	db = sqlite3.connect(dbfile)
	c = db.cursor()
	mac = raw_input('mac address or six-char prefix> ')
	pre = (''.join(i.upper() for i in mac if i in '0123456789aAbBcCdDfF'))[:6]
	c.execute('SELECT name FROM manuf WHERE prefix=?',(pre,))
	d = c.fetchone()
	if d:
		print d[0]
	else:
		print 'not found'
cmds.append(('macaddr','looks up the manufacturer associated with a MAC address',maclookup))

def portlookup():
	db = sqlite3.connect(dbfile)
	c = db.cursor()
	port = input('TCP or UDP port> ')
	c.execute('SELECT name FROM service WHERE port=? AND proto="tcp"',(port,))
	print 'TCP port {}:'.format(port)
	for i in c.fetchall():
		print i[0]
	c.execute('SELECT name FROM service WHERE port=? AND proto="udp"',(port,))
	print 'UDP port {}:'.format(port)
	for i in c.fetchall():
		print i[0]
cmds.append(('port','looks up the services running on a port',portlookup))

def subnet():
	pre = input('prefix length (CIDR notation)> ')
	print 'number of hosts:',num_hosts(pre)
	print 'subnet mask:',subnet_mask(pre)
cmds.append(('snprefix','calculates a subnet mask from a CIDR prefix length',subnet))

def network():
	net = raw_input('IP address> ')
	pre = input('prefix length (CIDR notation)> ')
	print 'network address:',network_address(net,pre)
	print 'broadcast address:',broadcast_address(net,pre)
	print 'number of hosts:',num_hosts(pre)
	print 'subnet mask:',subnet_mask(pre)
cmds.append(('subnet','calculates a network address from a CIDR prefix length',network))

def hostname():
	name = raw_input('IP address or hostname> ')
	try:
		hn,alias,ips = socket.gethostbyname_ex(name)
	except:
		hn,alias,ips = socket.gethostbyaddr(name)
	print 'hostname:',hn
	print 'ip addresses:',' '.join(ips)
	print 'other names:',' '.join(alias)
cmds.append(('hostname','looks up the hostname and other IP addresses of an address',hostname))
