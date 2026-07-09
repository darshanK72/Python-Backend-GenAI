# Google Gemini API Integration

| Approach | Folder | Best for |
|----------|--------|----------|
| **Console** | `01. Console Application/` | Learning the `google-genai` SDK |
| **FastAPI** | `02. Fast API Application/` | Production HTTP API |

Both read `GOOGLE_API_KEY` from the **repo root** `.env`. Optional local overrides: copy `02. Fast API Application/.env.example` to `.env` in that folder.

## Quick start

### Console

```bash
cd "01. Console Application"
python 01_chat_completion.py
```

### FastAPI

```bash
cd "02. Fast API Application"
uvicorn app.main:app --reload --port 8011
```

Open http://127.0.0.1:8011/docs

## What each approach covers

| Topic | Console | FastAPI |
|-------|---------|---------|
| Chat completion | `01_chat_completion.py` | `POST /api/v1/chat` |
| Streaming | `02_streaming.py` | `POST /api/v1/chat/stream` |
| Token counting | `03_token_count.py` | `POST /api/v1/usage/tokens/count` |
| Rate-limit retries | — | `GeminiService._call_with_retry()` |
| HTTP error mapping | — | `GeminiService.map_error()` |
