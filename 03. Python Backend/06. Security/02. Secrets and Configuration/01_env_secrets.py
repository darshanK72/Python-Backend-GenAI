# 01 — Load secrets from environment variables
# Run: python 01_env_secrets.py

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[3] / ".env")
except ImportError:
    pass

# Never hardcode in source:
# API_KEY = "sk-live-...."   # BAD

api_key = os.getenv("OPENAI_API_KEY", "")
db_password = os.getenv("MYSQL_PASSWORD", "")
secret_key = os.getenv("SECRET_KEY", "")

if __name__ == "__main__":
    print("API key set:", bool(api_key))
    print("DB password set:", bool(db_password))
    print("SECRET_KEY set:", bool(secret_key))
    print("Template: config.example.env at repo root")
