# Gen AI Capstone — RAG API over FastAPI
# Run: uvicorn app:app --port 8030
# Install: pip install fastapi uvicorn chromadb openai
# Requires: OPENAI_API_KEY in repo root .env

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

app = FastAPI(title="Gen AI RAG Capstone")

DOCS = [
    "The Notes API is a FastAPI project for learning REST CRUD.",
    "Redis can be used as a cache and message broker.",
    "pytest is the standard test runner for Python backends.",
]
_collection = None


class Question(BaseModel):
    question: str = Field(min_length=3, max_length=500)


def get_collection():
    global _collection
    if _collection is not None:
        return _collection
    try:
        import chromadb
    except ImportError:
        raise HTTPException(501, "Install chromadb")

    client = chromadb.Client()
    _collection = client.get_or_create_collection("capstone")
    _collection.add(ids=[str(i) for i in range(len(DOCS))], documents=DOCS)
    return _collection


def rag_answer(question: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise HTTPException(500, "OPENAI_API_KEY not configured")

    from openai import OpenAI

    col = get_collection()
    hits = col.query(query_texts=[question], n_results=2)
    context = "\n".join(hits["documents"][0])

    client = OpenAI(api_key=key)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer from context only. Be brief."},
            {"role": "user", "content": f"Context:\n{context}\n\nQ: {question}"},
        ],
    )
    return resp.choices[0].message.content or ""


@app.get("/health")
def health():
    return {"status": "ok", "openai_configured": bool(os.getenv("OPENAI_API_KEY"))}


@app.post("/ask")
def ask(payload: Question):
    return {"question": payload.question, "answer": rag_answer(payload.question)}
