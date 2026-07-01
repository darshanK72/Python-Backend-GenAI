# 03 — RAG pipeline steps
# Run: python 03_rag_pipeline.py

STEPS = [
    "Load documents (PDF, markdown, DB)",
    "Chunk text with overlap",
    "Embed chunks → vectors",
    "Store in vector database with metadata",
    "On query: embed question, retrieve top-k chunks",
    "Send chunks + question to LLM",
    "Return answer with optional citations",
]

if __name__ == "__main__":
    print("RAG pipeline:\n")
    for i, step in enumerate(STEPS, 1):
        print(f"  {i}. {step}")
