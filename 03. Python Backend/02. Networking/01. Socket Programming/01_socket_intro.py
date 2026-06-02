# 01 — Sockets (introduction)
# Run: python 01_socket_intro.py
#
# Sockets let programs send bytes over a network (TCP/UDP).
# HTTP and databases use sockets under the hood.

import socket

# --- 1. Create a socket (IPv4, TCP) ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created:", s)

# --- 2. Common families and types ---
print("AF_INET = IPv4, SOCK_STREAM = TCP, SOCK_DGRAM = UDP")

s.close()
print("socket closed")
