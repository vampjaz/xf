import sys, tty, termios, codecs, unicodedata, re, time, os
from contextlib import contextmanager

desc = 'self-explanatory'
author = 'nwx'
cmds = []

def hackertyper():
	@contextmanager
	def cbreak():
		old_attrs = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin)
		try:
			yield
		finally:
			termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attrs)
	def uinput():
		reader = codecs.getreader(sys.stdin.encoding)(sys.stdin)
		with cbreak():
			while True:
				yield reader.read(1)
	def is_interrupt(c):
		return c == '\x04'

	data = open(os.path.join(os.path.dirname(__file__),'data/hack.txt')).read()
	strs = re.split(r'(\s+)',data)
	it = iter(strs)

	try:
		for c in uinput():
				if is_interrupt(c):
					break
				else:
					try:
						sys.stdout.write(it.next())
						sys.stdout.flush()
					except StopIteration:
						it = iter(strs)
	except:
		print
		print
		time.sleep(0.1)
		print '======================'
		time.sleep(0.1)
		print "====ACCESS GRANTED===="
		time.sleep(0.1)
		print '======================'
		time.sleep(0.1)
		print
cmds.append(('1337','hacker typer in a real terminal',hackertyper))
