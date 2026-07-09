# 03 — Count tokens with Gemini API, then generate (console)
# Run: python 03_token_count.py
# Requires: GOOGLE_API_KEY in repo root .env

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_env import require_key

from google import genai

api_key = require_key("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit(1)

MODEL = "gemini-2.0-flash"
prompt = "Explain recursion in programming in two short paragraphs."

client = genai.Client(api_key=api_key)

count_result = client.models.count_tokens(model=MODEL, contents=prompt)
print(f"Prompt tokens (Gemini API): {count_result.total_tokens}")

response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
    config={"max_output_tokens": 300, "temperature": 0.3},
)

print("\nAssistant:", (response.text or "")[:200], "...")

if response.usage_metadata:
    meta = response.usage_metadata
    print(
        f"\nAPI usage — input: {meta.prompt_token_count}, "
        f"output: {meta.candidates_token_count}"
    )
