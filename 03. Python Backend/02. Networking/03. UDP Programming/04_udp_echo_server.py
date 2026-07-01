# 04 — UDP echo (multiple messages)
# Run: python 04_udp_echo_server.py
# Then: python 04_udp_echo_client.py

import socket

HOST = "127.0.0.1"
PORT = 9998

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Echo server on {HOST}:{PORT} (send 'quit' to stop)")

    while True:
        data, addr = sock.recvfrom(1024)
        text = data.decode()
        print("Received:", text, "from", addr)
        if text.lower() == "quit":
            sock.sendto(b"bye", addr)
            break
        sock.sendto(data.upper(), addr)

    sock.close()
