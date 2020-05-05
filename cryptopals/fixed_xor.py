#!/usr/bin/env python3

import codecs
from binascii import unhexlify, b2a_base64
from pwn import xor

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

string1 = codecs.decode('1c0111001f010100061a024b53535009181c', 'hex')

print('string1: %s ' % string1)

string2 = codecs.decode('686974207468652062756c6c277320657965', 'hex')

print('string2: %s ' % string2)

# xored = xor(string1, string2)

# https://stackoverflow.com/a/36242949

def xor_two_str(a, b):
	return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

xor_2 = xor_two_str(str1, str2)
print(xor_2)

print(bytes.fromhex(xor_2))

# result = codecs.encode(codecs.decode(xored, 'hex'), 'base64').decode().strip('\n')

print("string1 XOR'd against string2 should get")

print(xor(string1, string2))
# print(xored)