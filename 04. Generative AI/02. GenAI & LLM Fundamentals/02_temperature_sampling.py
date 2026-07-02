# 02 — Temperature and sampling
# Run: python 02_temperature_sampling.py

import random

VOCAB = ["the", "cat", "sat", "on", "mat", "dog", "ran"]


def sample_next_token(temperature: float) -> str:
    """Lower temperature -> more deterministic choice."""
    weights = [1.0] * len(VOCAB)
    if temperature < 0.5:
        weights[0] = 5.0  # favor 'the'
    scaled = [w ** (1 / max(temperature, 0.1)) for w in weights]
    return random.choices(VOCAB, weights=scaled, k=1)[0]


if __name__ == "__main__":
    random.seed(42)
    for temp in [0.2, 1.0, 1.5]:
        picks = [sample_next_token(temp) for _ in range(5)]
        print(f"temperature={temp}: {picks}")
