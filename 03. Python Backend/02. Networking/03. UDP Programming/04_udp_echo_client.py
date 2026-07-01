# 04 — UDP echo client
# Run: python 04_udp_echo_client.py  (start 04_udp_echo_server.py first)

import socket

HOST = "127.0.0.1"
PORT = 9998

messages = ["hello", "udp", "quit"]

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for msg in messages:
    client.sendto(msg.encode(), (HOST, PORT))
    reply, _ = client.recvfrom(1024)
    print(f"Sent: {msg!r} -> {reply.decode()!r}")
client.close()
