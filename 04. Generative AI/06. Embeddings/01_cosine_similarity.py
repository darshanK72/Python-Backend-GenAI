# 01 — Cosine similarity between vectors
# Run: python 01_cosine_similarity.py

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


if __name__ == "__main__":
    python_vec = [1.0, 0.8, 0.2, 0.0]
    java_vec = [0.9, 0.7, 0.1, 0.0]
    cooking_vec = [0.0, 0.1, 0.2, 1.0]
    print("python vs java:", round(cosine_similarity(python_vec, java_vec), 3))
    print("python vs cooking:", round(cosine_similarity(python_vec, cooking_vec), 3))
