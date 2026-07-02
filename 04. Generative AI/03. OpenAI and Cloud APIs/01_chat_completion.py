# 01 — Chat completion with roles
# Run: python 01_chat_completion.py
# Install: pip install openai

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


def chat(client: OpenAI, user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be brief."},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Set OPENAI_API_KEY in .env")
        raise SystemExit(1)
    client = OpenAI(api_key=key)
    print(chat(client, "Name three Python web frameworks."))
