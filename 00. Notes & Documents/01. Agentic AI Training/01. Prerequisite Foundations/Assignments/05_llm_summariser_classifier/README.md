# Assignment 05 — LLM Summariser & Classifier Service

Capstone FastAPI service with secured LLM-backed `/summarise` and `/classify` endpoints.

**Problem statement:** [llm_summariser_assignment.md](llm_summariser_assignment.md)

## Project layout

```
05_llm_summariser_classifier/
├── llm_summariser_assignment.md
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py          # X-API-Key auth + LLM service DI
│   ├── endpoints/health.py
│   ├── endpoints/llm.py         # /summarise, /classify
│   ├── schemas/                 # request + response models + prompts
│   └── services/llm_service.py
└── tests/
```

## Setup

```bash
cd "00. Notes & Documents/MAS_Foundation_Assignments/05_llm_summariser_classifier"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Add OPENAI_API_KEY and optionally change LLM_SERVICE_API_KEY
```

## Run

```bash
fastapi dev app/main.py --port 8022
```

Docs: http://127.0.0.1:8022/docs

## Auth

Both POST endpoints require:

```
X-API-Key: demo-key
```

(Set `LLM_SERVICE_API_KEY` in `.env` to change the expected key.)

## Sample requests

### POST /summarise → 200

```bash
curl -X POST http://127.0.0.1:8022/summarise ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Long paragraph about sprint planning, blockers, and release timelines...\"}"
```

```json
{"summary": "Team discussed sprint blockers and release timing.", "word_count": 8}
```

### POST /classify (bug report) → 200

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"The app crashes when I tap save on the settings page.\"}"
```

```json
{"category": "bug", "confidence": 0.93, "rationale": "Reports a reproducible crash."}
```

### POST /classify with no key → 401

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Can we add dark mode?\"}"
```

### POST /summarise with empty text → 422

```bash
curl -X POST http://127.0.0.1:8022/summarise ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"\"}"
```

## Tests

Tests mock the LLM client — no network calls required:

```bash
pytest tests/ -v
```

## Failure handling

- Invalid LLM JSON → one corrective retry, then HTTP **502**
- Empty `text` → HTTP **422** via Pydantic
- Invalid `category` values from the model are rejected → HTTP **502**
- Missing/wrong `X-API-Key` → HTTP **401**
