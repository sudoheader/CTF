#!/usr/bin/env python3

import binascii
from itertools import cycle

def do_xor(key, message):
	message = binascii.unhexlify(message.replace(' ', ''))
	key = binascii.unhexlify(''.join(key.split()[::-1]))

	return ''.join([chr(a ^ b) for a,b in zip(message, cycle(key))])

with open('hexoneline', 'r') as f:
	message = f.read()
f.close()

# message is the hex signature for a .jpg file
message = "FFD8FFE000104A4649460001"
key = "46ccf9a571f0ffb17e41cb84"

print(binascii.hexlify(do_xor(key,message).encode('utf-8')))

#http://opentechnotes.blogspot.com/2014/08/xor-string-with-key-in-python.html
