# 03 — Hallucinations and limitations
# Run: python 03_hallucinations.py

if __name__ == "__main__":
    print("LLMs predict likely text — they do not guarantee truth.")
    print("\nMitigations:")
    print("  - RAG: ground answers in your documents")
    print("  - Tool use: fetch live data from APIs/databases")
    print("  - Ask model to cite sources or say 'I don't know'")
    print("  - Evaluate outputs on a test set before shipping")
