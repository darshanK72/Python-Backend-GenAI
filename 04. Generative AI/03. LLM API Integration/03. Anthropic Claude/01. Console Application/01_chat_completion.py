# 01 — Claude messages API (console)
# Run: python 01_chat_completion.py
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
MODEL = "claude-sonnet-4-20250514"

message = client.messages.create(
    model=MODEL,
    max_tokens=200,
    temperature=0.3,
    system="You are a concise technical writer.",
    messages=[
        {"role": "user", "content": "What is an API in two sentences?"},
    ],
)

text_parts = [block.text for block in message.content if block.type == "text"]
print("Assistant:", " ".join(text_parts))
print("Model:", message.model)
print("Stop reason:", message.stop_reason)

if message.usage:
    print(
        f"Tokens — input: {message.usage.input_tokens}, "
        f"output: {message.usage.output_tokens}"
    )

follow_up = client.messages.create(
    model=MODEL,
    max_tokens=150,
    messages=[
        {"role": "user", "content": "What is REST?"},
        {
            "role": "assistant",
            "content": "REST is an architectural style for web APIs using HTTP methods and resources.",
        },
        {"role": "user", "content": "Give one example of a REST endpoint."},
    ],
)
print("\nMulti-turn reply:", follow_up.content[0].text)
