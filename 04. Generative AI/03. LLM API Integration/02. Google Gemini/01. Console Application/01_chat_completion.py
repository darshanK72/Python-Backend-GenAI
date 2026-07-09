# 01 — Gemini chat completion (console)
# Run: python 01_chat_completion.py
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
MODEL = "gemini-2.0-flash"

response = client.models.generate_content(
    model=MODEL,
    contents="What is machine learning in one paragraph?",
    config={
        "temperature": 0.4,
        "max_output_tokens": 200,
        "system_instruction": "You are a concise technical writer.",
    },
)

print("Assistant:", response.text)
print("Model:", MODEL)

if response.usage_metadata:
    meta = response.usage_metadata
    print(
        f"Tokens — prompt: {meta.prompt_token_count}, "
        f"completion: {meta.candidates_token_count}, "
        f"total: {meta.total_token_count}"
    )

chat_response = client.models.generate_content(
    model=MODEL,
    contents=[
        {"role": "user", "parts": [{"text": "You are a helpful coding assistant."}]},
        {
            "role": "model",
            "parts": [{"text": "Understood. I will give clear, concise coding help."}],
        },
        {"role": "user", "parts": [{"text": "Show a Python hello world in one line."}]},
    ],
    config={"temperature": 0.3, "max_output_tokens": 150},
)

print("\nMulti-turn reply:", chat_response.text)
