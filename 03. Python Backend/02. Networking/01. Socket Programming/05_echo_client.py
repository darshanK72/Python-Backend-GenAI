# 05 — Echo client (interactive)
# Run: python 05_echo_client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9000))

msg = input("You: ")
while msg.strip().lower() != "bye":
    client.send(msg.encode())
    print("Server:", client.recv(1024).decode())
    msg = input("You: ")

client.send(b"bye")
client.close()
