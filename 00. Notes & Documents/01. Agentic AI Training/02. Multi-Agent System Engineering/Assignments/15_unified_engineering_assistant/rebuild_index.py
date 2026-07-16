"""Rebuild the FAISS index from Wikipedia articles."""

from app.config import FAISS_INDEX_DIR
from app.services.ingestion import chunk_documents, fetch_articles
from app.services.vector_store import VectorStore


# main - fetch, chunk, and persist the local FAISS knowledge-base index
def main() -> int:
    print("Fetching Wikipedia articles...")
    articles = fetch_articles()
    chunks = chunk_documents(articles)
    print(f"Built {len(chunks)} chunks from {len(articles)} articles.")
    VectorStore.build_and_save(chunks, FAISS_INDEX_DIR)
    print(f"Saved FAISS index to {FAISS_INDEX_DIR}")
    return 0


# main - run the FAISS rebuild CLI
if __name__ == "__main__":
    raise SystemExit(main())
