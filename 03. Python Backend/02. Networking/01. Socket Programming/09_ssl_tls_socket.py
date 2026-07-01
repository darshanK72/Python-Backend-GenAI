# 09 — TLS/SSL socket (HTTPS over raw socket)
# Run: python 09_ssl_tls_socket.py
# Needs: internet

import socket
import ssl

HOST = "www.python.org"
PORT = 443

context = ssl.create_default_context()

with socket.create_connection((HOST, PORT), timeout=10) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as tls_sock:
        request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
        tls_sock.sendall(request.encode())
        response = tls_sock.recv(400).decode(errors="replace")
        print("TLS cipher:", tls_sock.cipher())
        print("Response preview:\n", response[:300])
