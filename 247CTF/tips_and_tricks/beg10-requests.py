import requests

url = 'tcp://65c6538b01b07056.247ctf.com:50371'
# url = "65c6538b01b07056.247ctf.com:50371"
# port = 50371

# s = requests.Session()
# s.get(url)
# r = requests.get("tcp://65c6538b01b07056.247ctf.com:50371")
r = requests.get(url)

# response = client.recv(4096)
print(r)
