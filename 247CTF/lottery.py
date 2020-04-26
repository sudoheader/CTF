import random
import socket
import time

secret = random.random()

for i in range(0, 1000):
	secret.seed(int(time.time() + 1))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('ea1a6f07f6fba51c.247ctf.com', 50302))
	sock.recv(1024)
	guess = str(secret.random()).encode()
	sock.sendall(guess)
	res = str(sock.recv(1024))
	if 'Nope' not in res:
		print(res)
		break
	print(res)
	sock.close()