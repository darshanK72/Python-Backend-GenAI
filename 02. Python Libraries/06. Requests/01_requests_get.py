# 01 — requests GET
# Run: python 01_requests_get.py
# Install: pip install requests

import requests

# --- 1. Public test API (needs internet) ---
url = "https://httpbin.org/get"
params = {"course": "python", "lesson": 1}

response = requests.get(url, params=params, timeout=10)
print("status:", response.status_code)
print("ok:", response.ok)

data = response.json()
print("args:", data.get("args"))
print("url:", data.get("url"))

# --- 2. Response attributes ---
print("headers content-type:", response.headers.get("Content-Type"))

# --- 3. Error handling ---
try:
    bad = requests.get("https://httpbin.org/status/404", timeout=10)
    bad.raise_for_status()
except requests.HTTPError as e:
    print("HTTP error caught:", e.response.status_code)
