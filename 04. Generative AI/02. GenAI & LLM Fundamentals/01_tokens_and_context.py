# 01 — Tokens and context window
# Run: python 01_tokens_and_context.py

def rough_token_count(text: str) -> int:
    """Rough estimate: ~4 characters per token for English."""
    return max(1, len(text) // 4)


SAMPLE = "Generative AI models read input as tokens, not whole words."

if __name__ == "__main__":
    print("Text:", SAMPLE)
    print("Rough token estimate:", rough_token_count(SAMPLE))
    print("\nContext window = max tokens the model can see (prompt + completion).")
    print("Long documents must be chunked or summarized.")
