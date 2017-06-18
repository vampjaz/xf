import qrcode

desc = 'generates QR codes'
author = 'nwx'
cmds = []

def generate():
	txt = raw_input('text to encode> ')
	path = raw_input('path to write out file to (include an extension)> ').strip()
	img = qrcode.make(txt)
	img.save(path)
cmds.append(('qrcode','generate a qr code as an image',generate))
