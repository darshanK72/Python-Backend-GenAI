# 02 — TCP server (one message)
# Run: python 02_tcp_server.py
# Then in another terminal: python 03_tcp_client.py

import socket

HOST = "127.0.0.1"
PORT = 8999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print("Connected from:", addr)
conn.send(b"Welcome to the server!")
conn.close()
server.close()
