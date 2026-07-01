# 01 — Chroma in-memory vector store
# Run: python 01_chroma_basics.py
# Install: pip install chromadb

try:
    import chromadb
except ImportError:
    print("Install: pip install chromadb")
    raise SystemExit(1)

if __name__ == "__main__":
    client = chromadb.Client()
    collection = client.get_or_create_collection("lesson_docs")
    collection.add(
        ids=["1", "2"],
        documents=[
            "FastAPI is a modern Python web framework.",
            "Redis is an in-memory data store used for caching.",
        ],
        metadatas=[{"topic": "api"}, {"topic": "cache"}],
    )
    results = collection.query(query_texts=["Python web framework"], n_results=1)
    print("Top match:", results["documents"][0][0])
