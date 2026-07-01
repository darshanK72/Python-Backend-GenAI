# 02 — RAG with Chroma + OpenAI
# Run: python 02_rag_with_openai.py
# Install: pip install chromadb openai

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

try:
    import chromadb
    from openai import OpenAI
except ImportError:
    print("Install: pip install chromadb openai")
    raise SystemExit(1)

from knowledge_base import DOCUMENTS


def build_index():
    client = chromadb.Client()
    col = client.get_or_create_collection("rag_lesson")
    col.add(
        ids=[d["id"] for d in DOCUMENTS],
        documents=[d["text"] for d in DOCUMENTS],
        metadatas=[{"source": d["source"]} for d in DOCUMENTS],
    )
    return col


def rag_answer(question: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return "Set OPENAI_API_KEY in .env"

    col = build_index()
    hits = col.query(query_texts=[question], n_results=2)
    context = "\n".join(hits["documents"][0])

    client = OpenAI(api_key=key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Answer using only the context. If unsure, say you don't know.",
            },
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(rag_answer("What is Alembic used for?"))
