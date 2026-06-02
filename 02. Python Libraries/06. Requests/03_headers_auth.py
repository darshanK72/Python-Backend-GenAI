# 03 — Headers and API keys
# Run: python 03_headers_auth.py
#
# Never hardcode real API keys in source code.
# Use environment variables: os.environ["API_KEY"]

import os
import requests

headers = {
    "User-Agent": "PythonLearning/1.0",
    "Accept": "application/json",
}

# Example: read key from env (set in terminal before running)
api_key = os.environ.get("DEMO_API_KEY", "demo-key-not-real")
headers["Authorization"] = f"Bearer {api_key}"

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers,
    timeout=10,
)
print(response.json().get("headers", {}))

print("\nTip: use python-dotenv to load .env files (see 12. Utilities)")
