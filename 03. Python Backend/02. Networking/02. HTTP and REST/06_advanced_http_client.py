# 06 — Advanced HTTP client (auth, session, retries, timeout)
# Run: python 06_advanced_http_client.py
# Needs: internet

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
session.headers.update({"Accept": "application/json"})

retry = Retry(total=3, backoff_factor=0.3, status_forcelist=[502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Bearer token style header
token = "demo-token-123"
response = session.get(
    "https://httpbin.org/bearer",
    headers={"Authorization": f"Bearer {token}"},
    timeout=10,
)
print("Bearer auth response:", response.json())

# Query params + JSON POST in one session
post = session.post(
    "https://httpbin.org/post",
    params={"source": "lesson"},
    json={"task": "advanced-http", "ok": True},
    timeout=10,
)
print("Posted JSON:", post.json().get("json"))

# Timeout example (short timeout against slow endpoint)
try:
    session.get("https://httpbin.org/delay/5", timeout=1)
except requests.Timeout:
    print("Timeout caught as expected for delay/5 with timeout=1")

session.close()
