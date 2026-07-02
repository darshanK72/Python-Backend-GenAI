# 01 — Load API keys from environment
# Run: python 01_api_keys_env.py

import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

if __name__ == "__main__":
    print("OPENAI_API_KEY set:", bool(OPENAI_API_KEY))
    print("OPENAI_BASE_URL:", OPENAI_BASE_URL)
    print("\nAdd to repo root .env (see config.example.env)")
    if not OPENAI_API_KEY:
        print("Get a key from: https://platform.openai.com/api-keys")
