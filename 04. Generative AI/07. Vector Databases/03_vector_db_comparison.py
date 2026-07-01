# 03 — Vector database comparison
# Run: python 03_vector_db_comparison.py

OPTIONS = {
    "Chroma": "Easy local/dev, embedded, open source",
    "FAISS": "Fast similarity search library (Meta)",
    "Pinecone": "Managed cloud vector DB",
    "Weaviate": "Open source + cloud, hybrid search",
    "pgvector": "Postgres extension — vectors in SQL",
}

if __name__ == "__main__":
    print("Vector store options:\n")
    for name, detail in OPTIONS.items():
        print(f"  {name:12} {detail}")
