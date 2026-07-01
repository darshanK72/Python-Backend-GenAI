# 02 — SSE client (streaming HTTP)
# Run: python 02_sse_client.py  (start 01_sse_server.py first)

import requests

URL = "http://127.0.0.1:8787/events"

with requests.get(URL, stream=True, timeout=30) as response:
    response.raise_for_status()
    print("Listening for SSE events...")
    for line in response.iter_lines(decode_unicode=True):
        if line and line.startswith("data:"):
            print(line)
