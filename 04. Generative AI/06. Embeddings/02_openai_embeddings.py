# 02 — OpenAI embeddings API
# Run: python 02_openai_embeddings.py
# Install: pip install openai

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

try:
    from openai import OpenAI
except ImportError:
    print("Install: pip install openai")
    raise SystemExit(1)


def cosine(a: list[float], b: list[float]) -> float:
    import math

    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)


if __name__ == "__main__":
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Set OPENAI_API_KEY in .env")
        raise SystemExit(1)

    client = OpenAI(api_key=key)
    texts = ["Python FastAPI tutorial", "Baking sourdough bread"]
    resp = client.embeddings.create(model="text-embedding-3-small", input=texts)
    v0 = resp.data[0].embedding
    v1 = resp.data[1].embedding
    print("Similarity:", round(cosine(v0, v1), 4))
    print("Dimensions:", len(v0))
