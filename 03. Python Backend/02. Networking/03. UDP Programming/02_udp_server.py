# 02 — UDP server
# Run: python 02_udp_server.py
# Then: python 03_udp_client.py

import socket

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"UDP server on {HOST}:{PORT}")

data, addr = server.recvfrom(1024)
print("From:", addr, "Message:", data.decode())
server.sendto(b"Hello from UDP server", addr)
server.close()
