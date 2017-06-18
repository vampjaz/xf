from PIL import Image
import zbarlight

desc = 'tries to decode QR codes, barcodes, and some others automatically (requires zbar)'
author = 'nwx'
cmds = []

def decode():
	path = raw_input('path to image file> ').strip()
	with open(path, 'rb') as image_file:
		image = Image.open(image_file)
		image.load()
	for code in zbarlight.Symbologies.keys():
		codes = zbarlight.scan_codes(code,image)
		if codes:
			print '{}: {} found'.format(code,len(codes))
			for i in codes:
				print i
cmds.append(('qrdecode','decodes QR codes, barcodes, and a few others',decode))
