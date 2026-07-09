# OpenAI API Integration

Two ways to use the OpenAI Chat Completions API in this folder:

| Approach | Folder | Best for |
|----------|--------|----------|
| **Console** | `01. Console Application/` | Learning the SDK — direct, minimal code |
| **FastAPI** | `02. Fast API Application/` | Production patterns — HTTP API, layers, error handling |

Both read `OPENAI_API_KEY` from the **repo root** `.env`. Optional local overrides: copy `02. Fast API Application/.env.example` to `.env` in that folder.

## Quick start

### Console (direct SDK)

```bash
cd "01. Console Application"
python 01_chat_completion.py
```

### FastAPI (HTTP API)

```bash
cd "02. Fast API Application"
uvicorn app.main:app --reload --port 8010
```

Open http://127.0.0.1:8010/docs for interactive API docs.

## What each approach covers

| Topic | Console | FastAPI |
|-------|---------|---------|
| Chat completion | `01_chat_completion.py` | `POST /api/v1/chat` |
| Streaming | `02_streaming.py` | `POST /api/v1/chat/stream` |
| Token counting (tiktoken) | `03_token_count.py` | `POST /api/v1/usage/tokens/count` |
| Rate-limit retries | — | `OpenAIService._create_completion()` |
| HTTP error mapping | — | `OpenAIService.map_openai_error()` |
