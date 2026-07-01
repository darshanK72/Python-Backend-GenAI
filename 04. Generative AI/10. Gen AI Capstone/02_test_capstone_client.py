# 02 — Test capstone with requests
# Run: python 02_test_capstone_client.py
# Server must be running on port 8030

import json
import sys

try:
    import requests
except ImportError:
    print("Install: pip install requests")
    raise SystemExit(1)

BASE = "http://127.0.0.1:8030"


if __name__ == "__main__":
    try:
        health = requests.get(f"{BASE}/health", timeout=5)
        health.raise_for_status()
        print("Health:", health.json())

        if not health.json().get("openai_configured"):
            print("Warning: OPENAI_API_KEY not set — /ask will fail.")

        resp = requests.post(
            f"{BASE}/ask",
            json={"question": "What is the Notes API?"},
            timeout=60,
        )
        resp.raise_for_status()
        print("Answer:", json.dumps(resp.json(), indent=2))
    except requests.ConnectionError:
        print("Start server first: uvicorn app:app --port 8030")
        raise SystemExit(1)
