#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
	line = r.recvline()
	return json.loads(line.decode())

def json_send(hsh):
	request = json.dumps(hsh).encode()
	r.sendline(request)

received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

def test(rec):
	if(received["type"] == "bigint"):
		decode = len(received["encoded"])
		to_send = {
			"decoded": "bigint"
		}
		return int(received["type"], 16).to_bytes(decode, 'big').decode('ISO-8859-1').replace('\x00','')
	elif(received["type"] == "base64"):
		to_send = {
			"decoded": "base64"
		}
		return int(received["type"], 16).to_bytes(decode, 'big').decode('ISO-8859-1').replace('\x00','')
	elif(received["type"] == "hex"):
		to_send = {
			"decoded": "hex"
		}
	elif(received["type"] == "rot13"):
		to_send = {
			"decoded": "rot13"
		}
	elif(received["type"] == "utf-8"):
		to_send = {
			"decoded": "utf-8"
		}

json_send(to_send)

json_recv()
