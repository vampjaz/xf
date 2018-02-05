import os,sys

desc = 'provides the ability to traverse the filesystem'
author = 'nwx'
cmds = []

def chdir(args):
	if len(args) > 0:
		newdir = ' '.join(args)
	else:
		newdir = raw_input('directory to change to> ')
	relative = os.path.abspath(newdir)
	if not (newdir.startswith('/') or ':' in newdir) and os.path.exists(relative):
		os.chdir(relative)
	elif os.path.exists(newdir):
		os.chdir(newdir)
	else:
		print 'path does not exist'
cmds.append(('cd','change current working directory',chdir))

def getcdir():
	print os.getcwd()
cmds.append(('pwd','show full working directory',getcdir))

def listdir(args):
	if len(args) > 0:
		ldir = ' '.join(args)
	else:
		ldir = os.getcwd()
	if os.path.exists(ldir):
		for i in os.listdir(ldir):
			fullpath = os.path.join(ldir,i)
			size = os.path.getsize(fullpath)
			if os.path.isdir(fullpath):
				name = i+'/'
			elif os.path.islink(fullpath):
				name = i+'*'
			else:
				name = i
			print name,'\t\t',size
	else:
		print 'path does not exist'
cmds.append(('ls','lists the contents of the current directory',listdir))


'''
## NYI
def mkdir(args):
	pass
cmds.append(('mkdir','creates the speciied directory',mkdir))

def mkfile(args):
	pass
cmds.append(('touch','creates an empty file',mkfile))

def remove(args):
	pass
cmds.append(('rm','removes a file',remove))

def catfile(args):
	pass
cmds.append(('cat','prints the contents of a file',catfile))
'''
