# 02 — POST JSON data
# Run: python 02_post_json.py

import requests

url = "https://httpbin.org/post"
payload = {
    "name": "Darshan",
    "course": "Python Libraries",
    "topics": ["numpy", "pandas", "requests"],
}

response = requests.post(url, json=payload, timeout=10)
response.raise_for_status()
result = response.json()
print("posted json:", result.get("json"))
