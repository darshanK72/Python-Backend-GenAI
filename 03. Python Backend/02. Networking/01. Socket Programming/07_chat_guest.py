# 07 — Simple chat (guest connects)
# Run: python 07_chat_guest.py

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("127.0.0.1", 8999))

msg = input("Guest: ")
while msg.strip().lower() != "bye":
    soc.send(msg.encode())
    print("Host:", soc.recv(1024).decode())
    msg = input("Guest: ")

soc.close()
