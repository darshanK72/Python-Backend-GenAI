# 03 — Count tokens with Anthropic API, then generate (console)
# Run: python 03_token_count.py
# Requires: ANTHROPIC_API_KEY in repo root .env

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

import anthropic

api_key = require_key("ANTHROPIC_API_KEY")
if not api_key:
    raise SystemExit(1)

MODEL = "claude-sonnet-4-20250514"
prompt = "Explain recursion in programming in two short paragraphs."

client = anthropic.Anthropic(api_key=api_key)

count_result = client.messages.count_tokens(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
)
print(f"Prompt tokens (Anthropic API): {count_result.input_tokens}")

message = client.messages.create(
    model=MODEL,
    max_tokens=300,
    temperature=0.3,
    messages=[{"role": "user", "content": prompt}],
)

text = " ".join(b.text for b in message.content if b.type == "text")
print("\nAssistant:", text[:200], "...")

if message.usage:
    print(
        f"\nAPI usage — input: {message.usage.input_tokens}, "
        f"output: {message.usage.output_tokens}"
    )
