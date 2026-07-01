# 03 — UDP client
# Run: python 03_udp_client.py  (start 02_udp_server.py first)

import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello UDP", (HOST, PORT))
data, _ = client.recvfrom(1024)
print("Reply:", data.decode())
client.close()
