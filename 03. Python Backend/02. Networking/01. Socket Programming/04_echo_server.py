# 04 — Echo server (loop until client sends 'bye')
# Run: python 04_echo_server.py
# Client: python 05_echo_client.py

import socket

HOST = "127.0.0.1"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Echo server on", PORT)

conn, addr = server.accept()
print("Client:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data or data.strip().lower() == "bye":
        break
    print("Client said:", data)
    conn.send(f"Echo: {data}".encode())

conn.close()
server.close()
