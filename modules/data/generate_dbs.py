import sqlite3,os,sys

if len(sys.argv) != 2:
	print 'please specify nmap data directory as an argument'

path = sys.argv[1]

db = "nmap.db"

if os.path.exists(db):
	os.remove(db)

conn = sqlite3.connect(db)
c = conn.cursor()

c.execute("CREATE TABLE manuf (prefix text, name text)")
c.execute("CREATE TABLE service (port int, proto text, name text)")

fd = open(os.path.join(path,'nmap-mac-prefixes'))

for i in fd.readlines():
	if not i.startswith('#'):
		pre,name = i.split(' ',1)
		c.execute("INSERT INTO manuf VALUES (?,?)",(pre.strip(),name.strip()))

fd.close()

fd = open(os.path.join(path,'nmap-services'))

for i in fd.readlines():
	if not i.startswith('#'):
		t = i.split('\t')
		name = t[0].strip()
		port,proto = t[1].split('/')
		c.execute("INSERT INTO service VALUES (?,?,?)",(int(port),proto.strip(),name))

fd.close()

conn.commit()
conn.close()
