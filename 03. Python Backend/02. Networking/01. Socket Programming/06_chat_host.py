# 06 — Simple chat (host listens — run first)
# Run: python 06_chat_host.py
# Other terminal: python 07_chat_guest.py

import socket

HOST = "127.0.0.1"
PORT = 8999

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((HOST, PORT))
soc.listen(1)
print("Host waiting on port", PORT)

conn, addr = soc.accept()
print("Guest connected:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Guest:", data)
    reply = input("Host: ")
    if reply.strip().lower() == "bye":
        conn.send(reply.encode())
        break
    conn.send(reply.encode())

conn.close()
soc.close()
