# 02 — First OpenAI chat completion
# Run: python 02_first_chat_completion.py
# Install: pip install openai
# Requires: OPENAI_API_KEY in .env

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

try:
    from openai import OpenAI
except ImportError:
    print("Install: pip install openai")
    raise SystemExit(1)

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY in .env first.")
        raise SystemExit(1)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
        max_tokens=50,
    )
    print(response.choices[0].message.content)
