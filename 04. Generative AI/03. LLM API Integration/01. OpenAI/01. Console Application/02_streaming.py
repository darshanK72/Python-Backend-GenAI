# 02 — OpenAI streaming (console)
# Run: python 02_streaming.py
# Requires: OPENAI_API_KEY in repo root .env

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

from openai import OpenAI

api_key = require_key("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(1)

client = OpenAI(
    api_key=api_key,
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
)

print("Assistant (streaming): ", end="", flush=True)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "List three benefits of streaming LLM responses."},
    ],
    temperature=0.5,
    max_tokens=200,
    stream=True,
)

parts: list[str] = []
for chunk in stream:
    token = chunk.choices[0].delta.content
    if token:
        print(token, end="", flush=True)
        parts.append(token)

print(f"\n\nReceived {len(''.join(parts))} characters.")
