# 02 — Secrets in environment variables
# Run: python 02_env_secrets.py

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

# Never hardcode in source:
# API_KEY = "sk-live-...."   # BAD

api_key = os.getenv("OPENAI_API_KEY", "")
db_password = os.getenv("MYSQL_PASSWORD", "")

print("API key set:", bool(api_key))
print("DB password set:", bool(db_password))
print("Use config.example.env at repo root as template")
