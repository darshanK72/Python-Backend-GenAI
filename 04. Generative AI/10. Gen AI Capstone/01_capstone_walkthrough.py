# 01 — Capstone walkthrough
# Run: python 01_capstone_walkthrough.py

if __name__ == "__main__":
    print("Gen AI Capstone — RAG API")
    print("\n1. Set OPENAI_API_KEY in repo root .env")
    print("2. pip install fastapi uvicorn chromadb openai")
    print("3. uvicorn app:app --port 8030")
    print('4. POST /ask  {"question": "What is pytest?"}')
    print("5. GET  /health")
    print("\nCombines: FastAPI (backend) + Chroma (vectors) + OpenAI (LLM)")
