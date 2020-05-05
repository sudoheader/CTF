#!/usr/bin/env python3

# https://medium.com/@mucomplex/a-fun-platform-for-learning-modern-cryptography-series-1-95875c152b8d

#https://linuxconfig.org/how-to-parse-data-from-json-into-python
#https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#Crypto.Util.number.long_to_bytes
#https://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/

import json
import base64
import Crypto
from codecs import encode as rot13
from pwn import *

class decode_function(object):
	def __init__(self,data):
		self.key = ''
		self.value = ''
		loaded_json = json.loads(data)
		self.key = loaded_json['type']
		self.value = loaded_json['encoded']
		print('%s : %s' % (self.key,self.value))

	def calling(self):
		if self.key == 'base64':
			return base64.b64decode(self.value).decode('ISO-8859-1')
		elif self.key == "hex":
			return bytes.fromhex(self.value).decode('ISO-8859-1')
		elif self.key == "rot13":
			return rot13(self.value,'rot13')
		elif self.key == "bigint":
			len_decode = len(self.value)
			return int(self.value,16).to_bytes(len_decode, 'big').decode('ISO-8859-1').replace('\x00','')
		elif self.key == "utf-8":
			new_value = ''
			for i in self.value:
				new_value += chr(i)
			return new_value

p = connect('socket.cryptohack.org',13377)
for i in range(100):
	retrieve = p.recv_raw(1024)
	decoder = decode_function(retrieve)
	decode = decoder.calling()
	print('%d : %s ' % (i,decode))
	p.send('{"decoded":"'+decode+'"}')
	del decoder

print('\n\nthe flag is:'+p.recv(1024).decode('ISO-8859-1'))