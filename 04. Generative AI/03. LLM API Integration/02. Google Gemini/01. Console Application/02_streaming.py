# 02 — Gemini streaming (console)
# Run: python 02_streaming.py
# Requires: GOOGLE_API_KEY in repo root .env

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

from google import genai

api_key = require_key("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit(1)

client = genai.Client(api_key=api_key)

print("Assistant (streaming): ", end="", flush=True)

stream = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents="Explain three use cases for generative AI in education.",
    config={"temperature": 0.6, "max_output_tokens": 250},
)

parts: list[str] = []
for chunk in stream:
    if chunk.text:
        print(chunk.text, end="", flush=True)
        parts.append(chunk.text)

print(f"\n\nReceived {len(''.join(parts))} characters.")
