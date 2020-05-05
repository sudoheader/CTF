#!/usr/bin/env python

# I can show two ways of doing this
# one way is the long way and the other is using
# pwntools

from pwn import xor

message = "label"

lst = ''.join(str(ord(c)) for c in message)
print(lst)

key = chr(13)
encrypted = ''

# def xor(k, m):
# 	for i in len(lst):
# 		encrypted = ord(lst[i]) ^ key

# xor(key, lst)
res = xor(key, message)

# print(encrypted)
print(res)