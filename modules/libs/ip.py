class IPError(Exception):
	pass

def dotted_to_decimal(ipaddr):
	if not isinstance(ipaddr,str):
		raise IPError('dotted IP addresses must be strings')
	try:
		octets = [int(i) for i in ipaddr.split('.')]
	except:
		raise IPError('octets must be numbers')
	for i in octets:
		if i > 255 or i < 0:
			raise IPError('octets must be between 0 and 255, inclusive')
	if len(octets) != 4:
		raise IPError('IP addresses must have 4 octets')
	number = octets[3] + octets[2]*256 + octets[1]*65536 + octets[0]*16777216
	return number

def decimal_to_dotted(ipnum):
	if not isinstance(ipnum,int):
		raise IPError('IP address numbers must be ints')
	oc3 = ipnum % 256
	ipnum = ipnum/256
	oc2 = ipnum % 256
	ipnum = ipnum/256
	oc1 = ipnum % 256
	ipnum = ipnum/256
	oc0 = ipnum
	return "{}.{}.{}.{}".format(oc0,oc1,oc2,oc3)

def subnet_mask(prefixlen):
	if not isinstance(prefixlen,int) or prefixlen > 32 or prefixlen < 0:
		raise IPError('invalid prefix length')
	return decimal_to_dotted(int('1'*prefixlen + '0'*(32-prefixlen), 2))

def host_mask(prefixlen):
	if not isinstance(prefixlen,int) or prefixlen > 32 or prefixlen < 0:
		raise IPError('invalid prefix length')
	return decimal_to_dotted(int('0'*prefixlen + '1'*(32-prefixlen), 2))

def get_prefixlen(subnetmask):
	pass # have to figure this out later

def and_ip_addresses(ip1,ip2):
	if isinstance(ip1,str):
		ip1 = dotted_to_decimal(ip1)
	if isinstance(ip2,str):
		ip2 = dotted_to_decimal(ip2)
	return decimal_to_dotted(ip1 & ip2)

def or_ip_addresses(ip1,ip2):
	if isinstance(ip1,str):
		ip1 = dotted_to_decimal(ip1)
	if isinstance(ip2,str):
		ip2 = dotted_to_decimal(ip2)
	return decimal_to_dotted(ip1 | ip2)

def network_address(ip,prefixlen):
	return and_ip_addresses(ip,subnet_mask(prefixlen))

def broadcast_address(ip,prefixlen):
	return or_ip_addresses(ip,host_mask(prefixlen))

def is_in_network(network,prefixlen,ip):
	return network_address(network,prefixlen) == network_address(ip,prefixlen)

def num_hosts(prefixlen):
	return 2**(32-prefixlen) - 2

def iterate_ip_network(ip,prefixlen):
	network = network_address(ip,prefixlen)
	for i in range(1,num_hosts(prefixlen)-1):
		yield or_ip_addresses(network,i)



def iterate_ip_mask(mask): ## iterator for CIDR networks: 192.168.0.1/24
	ip,prefixlen = mask.split('/')
	prefixlen = int(prefixlen)
	network = network_address(ip,prefixlen)
	for i in range(1,num_hosts(prefixlen)-1):
		yield or_ip_addresses(network,i)

def iterate_port_mask(mask): ## iterator for simple port lists: 22,45-47,88,100-1000
	for i in mask.split(','):
		if '-' in i: #range
			a = i.split('-')
			for z in range(int(a[0]),int(a[-1])+1):
				yield z
		else:
			yield int(i)
