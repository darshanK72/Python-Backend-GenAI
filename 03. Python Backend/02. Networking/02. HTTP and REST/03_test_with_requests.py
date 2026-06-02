# 03 — Call a public API with requests
# Run: python 03_test_with_requests.py
# Needs: internet

import requests

response = requests.get("https://httpbin.org/get", params={"course": "backend"}, timeout=10)
print("status:", response.status_code)
print("json:", response.json())

# POST example
post = requests.post(
    "https://httpbin.org/post",
    json={"name": "Darshan", "role": "student"},
    timeout=10,
)
print("posted:", post.json().get("json"))
