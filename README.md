hi there

this is a bunch of penetration testing tools... i'm not responsible for what people do with them. this is meant to be educational

this doesn't cheat by simply running os.system() and using existing unix commands so it should in theory be cross platform

## deps:

    pip install pyping requests beautifulsoup pywhois scapy pypcap paramiko pillow qrcode zbarlight

it should be noted that the program will still work fine if you don't install all the dependencies. it will just disable the modules with unmet dependencies...

also follow instructions here to get scapy fully installed if it can't find dumbnet: https://stackoverflow.com/a/40924921

zbarlight needs extra dependencies that can't be installed with pip: http://zbar.sourceforge.net/

also i recommend getting some lists to use with it from https://github.com/danielmiessler/SecLists and https://github.com/danielmiessler/RobotsDisallowed

if anyone opens an issue asking how to use it without showing any indication of trying to solve it themselves, it will be deleted
