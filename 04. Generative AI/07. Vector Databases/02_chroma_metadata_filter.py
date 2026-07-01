# 02 — Metadata filters in vector search
# Run: python 02_chroma_metadata_filter.py
# Install: pip install chromadb

try:
    import chromadb
except ImportError:
    print("Install: pip install chromadb")
    raise SystemExit(1)

if __name__ == "__main__":
    client = chromadb.Client()
    col = client.get_or_create_collection("filtered")
    col.add(
        ids=["a", "b", "c"],
        documents=["Django ORM guide", "FastAPI dependency injection", "Django admin tips"],
        metadatas=[
            {"framework": "django"},
            {"framework": "fastapi"},
            {"framework": "django"},
        ],
    )
    results = col.query(
        query_texts=["web framework"],
        n_results=2,
        where={"framework": "django"},
    )
    print("Django-only matches:", results["documents"][0])
