# 10 — Socket troubleshooting
# Run: python 10_socket_troubleshooting.py

import socket

HOST = "127.0.0.1"
OPEN_PORT = 8999
CLOSED_PORT = 59999


def port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


print("Port check examples:")
print(f"  {HOST}:{OPEN_PORT} open? (start 02_tcp_server.py to test True)", port_open(HOST, OPEN_PORT))
print(f"  {HOST}:{CLOSED_PORT} open?", port_open(HOST, CLOSED_PORT))

print("\nCommon errors:")
print("  ConnectionRefusedError -> nothing listening on host:port")
print("  TimeoutError          -> firewall or wrong IP")
print("  WinError 10013        -> port in use or blocked on Windows")
print("  Address already in use -> set SO_REUSEADDR or pick another port")

try:
    bad = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bad.settimeout(1)
    bad.connect(("192.0.2.1", 80))  # TEST-NET, should not respond
except OSError as e:
    print("\nSimulated timeout/blocked connect:", type(e).__name__, e)
