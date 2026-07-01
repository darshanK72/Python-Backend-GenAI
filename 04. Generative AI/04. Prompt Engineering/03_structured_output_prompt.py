# 03 — Structured output instructions
# Run: python 03_structured_output_prompt.py

PROMPT = """
Extract order info as JSON with keys: product, quantity, city.
Return only valid JSON, no markdown.

Order: Please ship 3 keyboards to Pune.
"""

if __name__ == "__main__":
    print(PROMPT.strip())
    print("\nIn production use JSON mode / response_format / Pydantic with the API.")
