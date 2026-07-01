# 01 — UDP socket basics
# Run: python 01_udp_intro.py

import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("UDP socket created:", udp)
print("SOCK_DGRAM = connectionless, no handshake (unlike TCP)")
udp.close()
print("socket closed")
