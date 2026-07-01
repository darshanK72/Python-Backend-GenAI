# 03 — Chunking text for embeddings
# Run: python 03_text_chunking.py

def chunk_text(text: str, chunk_size: int = 200, overlap: int = 40) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


if __name__ == "__main__":
    doc = "RAG splits long documents into chunks. Each chunk is embedded and stored. "
    doc *= 5
    parts = chunk_text(doc, chunk_size=120, overlap=20)
    print(f"Chunks: {len(parts)}")
    for i, part in enumerate(parts[:3], 1):
        print(f"\n--- chunk {i} ({len(part)} chars) ---\n{part[:80]}...")
