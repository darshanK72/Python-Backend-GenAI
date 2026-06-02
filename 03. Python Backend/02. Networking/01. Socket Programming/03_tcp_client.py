# 03 — TCP client
# Run: python 03_tcp_client.py  (start 02_tcp_server.py first)

import socket

HOST = "127.0.0.1"
PORT = 8999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
data = client.recv(1024)
print("Received:", data.decode())
client.close()
