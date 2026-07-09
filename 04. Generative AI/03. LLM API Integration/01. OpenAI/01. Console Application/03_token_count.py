# 03 — Count tokens with tiktoken, then call the API (console)
# Run: python 03_token_count.py
# Requires: OPENAI_API_KEY in repo root .env

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

import tiktoken
from openai import OpenAI

api_key = require_key("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(1)

MODEL = "gpt-4o-mini"
prompt = "Explain recursion in programming in two short paragraphs."

try:
    encoding = tiktoken.encoding_for_model(MODEL)
except KeyError:
    encoding = tiktoken.get_encoding("cl100k_base")

print(f"Prompt tokens (tiktoken estimate): {len(encoding.encode(prompt))}")

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=300,
    temperature=0.3,
)

print("\nAssistant:", response.choices[0].message.content[:200], "...")

if response.usage:
    u = response.usage
    print(f"\nAPI usage — input: {u.prompt_tokens}, output: {u.completion_tokens}")
