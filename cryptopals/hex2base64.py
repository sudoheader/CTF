#!/usr/bin/env python3

# There are multiple ways of converting hex to base54 in python3

import codecs
from binascii import unhexlify, b2a_base64

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# METHOD 1:
# result = b2a_base64(unhexlify(hex_string)).decode().strip('\n')

# METHOD 2:
# result = b2a_base64(bytes.fromhex(hex_string)).decode().strip('\n')

# METHOD 3:
result = codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode().strip('\n')

print(result)

# https://stackoverflow.com/questions/33704327/hex-to-base64-conversion-in-python