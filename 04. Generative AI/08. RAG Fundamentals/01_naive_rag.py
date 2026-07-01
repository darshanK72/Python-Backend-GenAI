# 01 — Naive RAG without API (keyword retrieval demo)
# Run: python 01_naive_rag.py

from knowledge_base import DOCUMENTS


def retrieve(query: str, top_k: int = 2) -> list[str]:
    q = query.lower()
    scored = []
    for doc in DOCUMENTS:
        score = sum(1 for word in q.split() if word in doc["text"].lower())
        scored.append((score, doc["text"]))
    scored.sort(reverse=True)
    return [text for score, text in scored[:top_k] if score > 0]


def answer(query: str) -> str:
    chunks = retrieve(query)
    if not chunks:
        return "No relevant documents found."
    context = "\n".join(f"- {c}" for c in chunks)
    return f"Question: {query}\n\nContext:\n{context}\n\n(A real app sends context + question to an LLM.)"


if __name__ == "__main__":
    print(answer("How does Notes API work?"))
