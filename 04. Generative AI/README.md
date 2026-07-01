# Phase 4 — Generative AI

Use this section after **Python Fundamentals**, **Python Libraries**, and **Python Backend** (at least FastAPI + one database topic).

```bash
# repo root
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy [`../03. Python Backend/config.example.env`](../03.%20Python%20Backend/config.example.env) to repo root `.env` and set `OPENAI_API_KEY`.

## Learning path

| Order | Folder | Topics |
|-------|--------|--------|
| 1 | `01. AI Foundations/` | AI vs ML vs Gen AI, use cases, responsible AI (`01`–`03`) |
| 2 | `02. How LLMs Work/` | Tokens, temperature, hallucinations (`01`–`03`) |
| 3 | `03. Setup and API Keys/` | `.env`, first API call, cost estimate (`01`–`03`) |
| 4 | `04. Prompt Engineering/` | Roles, few-shot, structured output (`01`–`03`) |
| 5 | `05. OpenAI and Cloud APIs/` | Chat, streaming, providers (`01`–`03`) |
| 6 | `06. Embeddings/` | Cosine similarity, OpenAI embeddings, chunking (`01`–`03`) |
| 7 | `07. Vector Databases/` | Chroma, metadata filters, DB comparison (`01`–`03`) |
| 8 | `08. RAG Fundamentals/` | Naive RAG, Chroma+OpenAI RAG, pipeline (`01`–`03`) |
| 9 | `09. LangChain/` | LCEL chains, retriever, when to use (`01`–`03`) |
| 10 | `10. Gen AI Capstone/` | FastAPI RAG API (`01`–`02`) |

## Quick commands

**No API key needed:**
```bash
cd "04. Gen AI/01. AI Foundations"
python 01_ai_ml_genai.py

cd "../06. Embeddings"
python 01_cosine_similarity.py

cd "../07. Vector Databases"
python 01_chroma_basics.py
```

**Requires `OPENAI_API_KEY` in `.env`:**
```bash
cd "04. Gen AI/03. Setup and API Keys"
python 02_first_chat_completion.py

cd "../08. RAG Fundamentals"
python 02_rag_with_openai.py

cd "../10. Gen AI Capstone"
uvicorn app:app --port 8030
```

## Packages

Gen AI packages are in root `requirements.txt`: `openai`, `langchain`, `langchain-openai`, `langchain-chroma`, `chromadb`.

## Archived notebooks

Older lesson notebooks may live under `00. Notes & Documents/01. Notebooks/` — use this folder for new runnable `.py` lessons.
