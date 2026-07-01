# 08 — IP addresses and DNS
# Run: python 08_ip_and_dns.py

import ipaddress
import socket

# --- ipaddress module ---
net = ipaddress.ip_network("192.168.1.0/24")
host = ipaddress.ip_address("192.168.1.10")
print("Network:", net)
print("Host in network?", host in net)

# --- DNS lookup ---
hostname = "www.python.org"
infos = socket.getaddrinfo(hostname, 443, type=socket.SOCK_STREAM)
print(f"\nDNS for {hostname}:")
for family, socktype, proto, canonname, sockaddr in infos[:3]:
    print(" ", sockaddr)

# --- Reverse lookup (may fail for some IPs) ---
try:
    print("\nReverse:", socket.gethostbyaddr("8.8.8.8"))
except socket.herror:
    print("Reverse lookup unavailable")
