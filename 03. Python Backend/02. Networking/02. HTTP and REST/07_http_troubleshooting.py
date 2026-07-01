# 07 — HTTP troubleshooting
# Run: python 07_http_troubleshooting.py
# Needs: internet for most checks

import requests

checks = [
    ("200 OK", "https://httpbin.org/status/200"),
    ("404 Not Found", "https://httpbin.org/status/404"),
    ("500 Server Error", "https://httpbin.org/status/500"),
]

for label, url in checks:
    r = requests.get(url, timeout=10)
    print(f"{label}: HTTP {r.status_code}")

print("\nDiagnosing failures:")
try:
    requests.get("https://invalid.invalid.example", timeout=3)
except requests.exceptions.ConnectionError as e:
    print("ConnectionError (bad DNS/host):", type(e).__name__)

try:
    requests.get("https://httpbin.org/delay/10", timeout=1)
except requests.Timeout:
    print("Timeout: server too slow or network issue")

print("\nTips:")
print("  - 4xx = client/request problem (check URL, auth, body)")
print("  - 5xx = server problem")
print("  - Use response.raise_for_status() in scripts")
print("  - Log status code, response.text, and request URL")
