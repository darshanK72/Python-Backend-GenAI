# 02 — Streaming chat completion
# Run: python 02_streaming_completion.py
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


if __name__ == "__main__":
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Set OPENAI_API_KEY in .env")
        raise SystemExit(1)

    client = OpenAI(api_key=key)
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Count from 1 to 5 slowly."}],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
