import socket, time, sys, threading

desc = 'provides a tcp socket client and server similar to netcat'
author = 'nwx'
cmds = []

def connect():
	host = raw_input('host? ')
	port = input('port? ')
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		sock.connect((host,port))
		sock.setblocking(0)
		sock.settimeout(0.05)
		def readthread():
			try:
				while 1:
					sock.sendall(sys.stdin.read(1))
			except (socket.error,socket.herror,socket.gaierror,socket.timeout) as e:
				return
		t = threading.Thread(target=readthread)
		t.start()
		while 1:
			try:
				sys.stdout.write(sock.recv(1024))
				sys.stdout.flush()
			except socket.timeout as e:
				pass
	except socket.error as e:
		print 'socket error: ',repr(e)
	except (socket.herror,socket.gaierror,socket.timeout) as e:
		print 'could not connect: ',e
	except KeyboardInterrupt:
		print 'disconnecting'
cmds.append(('nc','connects to a tcp socket and provides a bidirectional communication channel (slightly broken)',connect))

def connectr():
	host = raw_input('host? ')
	port = input('port? ')
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		sock.connect((host,port))
		while True:
			sys.stdout.write(sock.recv(4096))
			time.sleep(0.005)
	except (socket.herror,socket.gaierror,socket.timeout) as e:
		print 'could not connect: ',e
	except KeyboardInterrupt:
		print 'disconnecting'
		sock.close()
cmds.append(('ncr','connects to a tcp socket and only reads data from it',connectr))

def server():
	port = input('port? ')
	serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		while True:
			serv.bind(('',port))
			serv.listen(1)
			sock,addr = sock.accept()
			sock.setblocking(0)
			sock.settimeout(0.05)
			def readthread():
				try:
					while 1:
						sock.sendall(sys.stdin.read(1))
				except (socket.error,socket.herror,socket.gaierror,socket.timeout) as e:
					return
			t = threading.Thread(target=readthread)
			t.start()
			while 1:
				try:
					sys.stdout.write(sock.recv(1024))
					sys.stdout.flush()
				except socket.timeout as e:
					pass
	except (socket.herror,socket.gaierror,socket.timeout) as e:
		print 'could not connect: ',e
	except KeyboardInterrupt:
		print 'disconnecting'
		sock.close()
cmds.append(('tcpserve','creates a tcp server that can accept one connection and provides a bidirectional communication channel (also somewhat broken)',server))

def listen():
	port = input('port? ')
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		while True:
			sock.bind(('',port))
			sock.listen(1)
			conn,addr = sock.accept()
			while True:
				sys.stdout.write(conn.recv(4096))
				time.sleep(0.005)
	except (socket.herror,socket.gaierror,socket.timeout) as e:
		print 'could not connect: ',e
	except KeyboardInterrupt:
		print 'disconnecting'
		sock.close()
cmds.append(('tcplisten','creates a tcp server that can accept connections and simply prints anything they send',listen))
