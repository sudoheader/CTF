import socket

# tcp://65c6538b01b07056.247ctf.com:50371
host = "65c6538b01b07056.247ctf.com"
port = "50371"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("GET / HTTP1.1\r\nHost: 247ctf.com\r\n\r\n")

response = client.recv(4096)
print(response)
