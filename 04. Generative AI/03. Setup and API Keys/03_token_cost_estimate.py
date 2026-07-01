# 03 — Estimate token cost
# Run: python 03_token_cost_estimate.py

def estimate_cost(input_tokens: int, output_tokens: int, price_in: float, price_out: float) -> float:
    return (input_tokens / 1_000_000 * price_in) + (output_tokens / 1_000_000 * price_out)


if __name__ == "__main__":
    # Example rates — check current pricing on provider site
    cost = estimate_cost(input_tokens=1200, output_tokens=400, price_in=0.15, price_out=0.60)
    print(f"Estimated cost: ${cost:.6f}")
    print("\nTrack usage in provider dashboard; set billing limits.")
