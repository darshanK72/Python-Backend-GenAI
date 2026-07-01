# 05 — HTTPS and SSL with requests
# Run: python 05_https_and_ssl.py
# Needs: internet

import requests

# Verified HTTPS (default)
r = requests.get("https://httpbin.org/get", timeout=10)
print("HTTPS status:", r.status_code)
print("URL:", r.url)

# Inspect TLS certificate info via underlying connection is limited in requests;
# use verify=True (default) in production.
print("verify=True by default (checks server certificate)")

# Custom headers over HTTPS
headers = {"User-Agent": "backend-lesson/1.0"}
r2 = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)
print("Sent User-Agent:", r2.json().get("headers", {}).get("User-Agent"))

# Never disable verify in production; shown for debugging only:
# requests.get(url, verify=False)
