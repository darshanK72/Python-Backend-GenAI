# 02 — Claude streaming (console)
# Run: python 02_streaming.py
# Requires: ANTHROPIC_API_KEY in repo root .env

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

import anthropic

api_key = require_key("ANTHROPIC_API_KEY")
if not api_key:
    raise SystemExit(1)

client = anthropic.Anthropic(api_key=api_key)

print("Assistant (streaming): ", end="", flush=True)

parts: list[str] = []
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=250,
    temperature=0.5,
    messages=[
        {
            "role": "user",
            "content": "List three benefits of streaming LLM responses.",
        },
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        parts.append(text)

print(f"\n\nReceived {len(''.join(parts))} characters.")
