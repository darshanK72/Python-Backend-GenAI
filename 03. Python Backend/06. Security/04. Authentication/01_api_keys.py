# 01 — API key authentication pattern
# Run: python 01_api_keys.py

import os
import secrets
from functools import wraps

VALID_API_KEYS = {os.getenv("LESSON_API_KEY", "demo-key-change-me")}


def require_api_key(handler):
    @wraps(handler)
    def wrapper(headers: dict, *args, **kwargs):
        key = headers.get("X-API-Key", "")
        if not any(secrets.compare_digest(key, valid) for valid in VALID_API_KEYS):
            return 401, {"error": "invalid or missing API key"}
        return handler(headers, *args, **kwargs)

    return wrapper


@require_api_key
def get_notes(headers: dict):
    return 200, {"notes": ["Buy milk", "Learn security"]}


if __name__ == "__main__":
    print("No key:", get_notes({}))
    print("Bad key:", get_notes({"X-API-Key": "wrong"}))
    print("Good key:", get_notes({"X-API-Key": "demo-key-change-me"}))
