# 01 — OpenAI chat completion (console)
# Run: python 01_chat_completion.py
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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a concise Python tutor."},
        {"role": "user", "content": "What is a list comprehension in one sentence?"},
    ],
    temperature=0.3,
    max_tokens=150,
)

choice = response.choices[0]
print("Assistant:", choice.message.content)
print("Model:", response.model)
print("Finish reason:", choice.finish_reason)

if response.usage:
    u = response.usage
    print(
        f"Tokens — prompt: {u.prompt_tokens}, "
        f"completion: {u.completion_tokens}, total: {u.total_tokens}"
    )
