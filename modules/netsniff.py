from scapy.all import *

desc = 'provides sniffing of different protocols using scapy'
author = 'nwx'
cmds = []

def packet_summary():
	iface = raw_input('interface to sniff on (leave blank for all)> ')
	if iface:
		sniff(iface=iface, prn=lambda x: x.summary())
	else:
		sniff(prn=lambda x: x.summary())
cmds.append(('packets','sniffs packets on the specified interface and prints their layers',packet_summary))

def packet_ip():
	iface = raw_input('interface to sniff on (leave blank for all)> ')
	if iface:
		sniff(iface=iface, prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
	else:
		sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
cmds.append(('packetip','sniffs packets on the specified interface and prints their ip addresses',packet_ip))
