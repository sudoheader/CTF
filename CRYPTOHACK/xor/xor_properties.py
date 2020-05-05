#!/usr/bin/env python3

from pwn import xor

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# First decode from hex to bytes
KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

print("KEY1 encoded %s" % KEY1)
decodedKEY1 = bytes.fromhex(KEY1)
print("KEY1 decoded %s" % decodedKEY1)

# key 2 xor with key 1
key21 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'

# flag xor key1 xor key3 xor key2
flag132 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# trying to find flag
flag = ''

KEY2 = ''

op1 = xor(KEY1, KEY2)
print(key21)

KEY3 = ''

# KEY2 and KEY3 are unknown. We can use pwntools to
# get keys.

# xor(KEY1, KEY2)