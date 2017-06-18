import socket, time, sys

desc = 'provides a tcp socket client and server similar to netcat'
author = 'nwx'
cmds = []

def connect():
	host = raw_input('host? ')
	port = input('port? ')
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		sock.connect((host,port))
		print "not yet implemented" ##################################################### TODO
		return
	except (socket.herror,socket.gaierror,socket.timeout) as e:
		print 'could not connect: ',e
	except KeyboardInterrupt:
		print 'disconnecting'
		sock.close()
cmds.append(('nc','connects to a tcp socket and provides a bidirectional communication channel',connect))

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
	print "not yet implemented"
cmds.append(('tcpserve','creates a tcp server that can accept one connection and provides a bidirectional communication channel',server))

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
