#!/usr/bin/env python3

import re
from pwn import *

# tcp://fa289d994e03263f.247ctf.com:50196
url = 'fa289d994e03263f.247ctf.com'
port = 50196
conn = remote(url, port)

# do this two times to get the first addition problem
print(conn.recvline())
print(conn.recvline())

# it will ask us to solve 500 addition problems.
for i in range(500):
	problem = conn.recvline().decode('utf-8')

	a = int(problem.split()[5])
	b = int(problem.split()[7].strip('?'))

	# we need to append str('\r\n') sendline requires str('\r') to work properly
	# result = (str(a + b) + str('\r')).encode('utf-8')
	result = (str(a + b) + str('\r\n')).encode('utf-8')
	conn.sendline(result)

	print("Problem: ", i + 1)
	print(a, " + ", b, " = ", result.decode('utf-8'))
	print(conn.recvline())
print(conn.recvline())

conn.close()