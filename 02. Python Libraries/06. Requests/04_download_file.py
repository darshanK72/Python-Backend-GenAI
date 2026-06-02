# 04 — Download binary content
# Run: python 04_download_file.py

import requests
import os

url = "https://httpbin.org/image/png"
response = requests.get(url, timeout=15)
response.raise_for_status()

path = "downloaded.png"
with open(path, "wb") as f:
    f.write(response.content)

print("saved", path, "bytes:", len(response.content))
os.remove(path)
