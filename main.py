#!/usr/bin/python
# coding=utf-8

## XF - exploit and whatever else framework
## better than all the rest that i've seen because they suck
## by nwx (tw:@nwx_hax, ig:@nwx.py, gh:red-green)

import os, sys, platform, argparse, time

# parse cli options

# parser = argparse.ArgumentParser(description='XF exploit framework')
# parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="print detailed status messages to stdout")
# parser_args = parser.parse_args()
# VERB = parser_args.verbose
VERB = False

# dynamic module loading that doesn't break everything if one is missing deps

modreport = []
modules = {}
commands = {}

loadstart = time.time()
errors = 0

filenames = [i for i in os.listdir(os.path.join(os.getcwd(),'modules')) if i.endswith('.py')]
basedir = os.path.join(os.getcwd(),'modules')

for fn in filenames:
	try:
		if VERB: print 'scanning',fn
		if os.path.isfile(os.path.join(basedir,fn)):
			if VERB: print ' it looks like a file!'
			modname = 'modules.' + fn.rsplit('.py',1)[0]
			exec('import {} as tempmod'.format(modname))
			if VERB: print ' successfully imported',fn
			for cmd,desc,func in tempmod.cmds:
				commands[cmd] = (fn,desc,func)
				if VERB: print ' loaded command',cmd,'-',desc
			modules[fn] = tempmod
			modreport.append('{} was successfully loaded'.format(fn))
		else:
			if VERB: print ' actually a directory:',
	except ImportError, e:
		if VERB:
			print ' could not import:'
			print ' ',e
			print ' perhaps the dependencies are not installed...'
		modreport.append('{} failed due to unsatasfied dependencies: {}'.format(fn,e))
		errors += 1
	except AttributeError, e:
		if VERB:
			print ' could not parse:'
			print ' ',e
			print ' perhaps the module is malformed...'
		modreport.append('{} failed due to malformed module: {}'.format(fn,e))
		errors += 1
	except Exception, e:
		if VERB:
			print ' could not load:'
			print ' ',e
		modreport.append('{} failed due to other error: {}'.format(fn,e))
		errors += 1

print 'loaded {} modules containing {} commands in {} seconds with {} unloaded due to errors!'.format(len(modules),len(commands),time.time()-loadstart,errors)

# builtin commands:

def help():
	print 'Command listing:'
	for i in sorted(commands.keys()):
		print '{} - {} (from {})'.format(i.ljust(15),commands[i][1],commands[i][0])
commands['help'] = ('_builtin','displays the list of commands',help)

def modlist():
	print 'Modules loaded:'
	for i in modules:
		print '{} - {} (by {})'.format(i.ljust(15),modules[i].desc,modules[i].author)
commands['modules'] = ('_builtin','displays the loaded modules',modlist)

def reports():
	print 'Module reports:'
	for i in modreport:
		print i
commands['report'] = ('_builtin','displays the module loading reports',reports)

#### todo: work on directory changing, listing, basic file stuff

# banner
print '@@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@\n@@@@ @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@\n@@!@!@@@  @@!  @@!  @@!  @@!  !@@  @@!\n!@!!@!@!  !@!  !@!  !@!  !@!  @!!  !@!\n@!@ !!@!  @!!  !!@  @!@   !@@!@!   @!!!:!\n!@!  !!!  !@!  !!!  !@!    @!!!    !!!!!:\n!!:  !!!  !!:  !!:  !!:   !: :!!   !!:\n:!:  !:!  :!:  :!:  :!:  :!:  !:!  :!:\n ::   ::   :::: :: :::    ::  :::   ::\n::    :     :: :  : :     :   ::    :  '
print 'by nwx (tw:@nwx_hax, ig:@nwx.py, gh:red-green)'
print 'try `help` for a list of commands'
print

# main command loop

while True:
	cmd = raw_input("> ")
	mod,desc,func = commands.get(cmd,('','',False))
	if func:
		try:
			func()
		except KeyboardInterrupt:
			print 'returning to main menu...'
	else:
		print 'that command does not seem to exist. look at the available commands with `help` or see why a module may not have loaded with `report`'
