# echo-server.py

import socket

HOST = "jdiaz.inf.santiago.usm.cl"  # Standard loopback interface address (localhost)
PORT = 50005# Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

buffer = (235*2)*3
msg = "GET 1/2 IMG ID:8".encode()

s.sendto(msg, (HOST, PORT))
response = s.recvfrom(buffer)[0]

image = open("image.png", "wb") 
image.write(response)