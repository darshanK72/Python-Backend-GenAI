# 02 — python-dotenv (.env files)
# Run: python 02_python_dotenv.py
# Install: pip install python-dotenv

import os
from pathlib import Path

# --- 1. Create a sample .env for demo ---
env_path = Path(".env.demo")
env_path.write_text(
    "APP_NAME=LearningPython\n"
    "DEBUG=true\n"
    "API_KEY=demo-not-real-key\n",
    encoding="utf-8",
)

from dotenv import load_dotenv

load_dotenv(env_path)
print("APP_NAME:", os.getenv("APP_NAME"))
print("DEBUG:", os.getenv("DEBUG"))
print("API_KEY set:", bool(os.getenv("API_KEY")))

# --- 2. Default if missing ---
print("MISSING:", os.getenv("MISSING", "default-value"))

env_path.unlink()
print("removed .env.demo")

# Real projects: add .env to .gitignore — never commit secrets.
