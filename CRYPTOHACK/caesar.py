#!/usr/bin/env python3

# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

message = 'RTGXGPV RTKOCTA IWKVCT VJGOG'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(letters)):
	translated = ''
	for symbol in message:
		if symbol in letters:
			num = letters.find(symbol)
			num = num - key
			if num < 0:
				num = num + len(letters)
			translated = translated + letters[num]
		else:
			translated = translated + symbol
	print('Hacking key #%s: %s' % (key, translated))