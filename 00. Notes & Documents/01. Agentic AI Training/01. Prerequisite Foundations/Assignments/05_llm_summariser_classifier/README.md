# Assignment 05 — LLM Summariser & Classifier Service

**Track:** GenAI + FastAPI · **Difficulty:** Medium · **Marks:** 10 · **Est. time:** ~3 hrs

Capstone FastAPI service combining structured LLM prompts, Pydantic validation, API-key auth, and robust failure handling — the exact shape of an MAS agent tool.

**Problem statement:** [`llm_summariser_assignment.md`](llm_summariser_assignment.md)

---

## Overview

A team needs an internal service that takes raw text and returns a clean summary and a category tag, behind a secured endpoint. This project ties together all three foundation tracks: FastAPI service design (Tracks 1–2), structured prompting and LLM API calls (Track 3), with auth reused from Assignment 03.

### What you will practice

- FastAPI endpoints backed by LLM calls
- Structured JSON prompts parsed into Pydantic models
- `X-API-Key` auth via `Depends`
- JSON retry with corrective hints → HTTP 502
- Category validation (allowed enum values)
- `TestClient` tests with mocked LLM

### Tech stack

| Component | Choice |
|-----------|--------|
| Framework | FastAPI |
| LLM | OpenAI chat-completions |
| Validation | Pydantic |
| Auth | `X-API-Key` header via `Depends` |
| Tests | pytest + TestClient (mocked LLM) |

---

## Project structure

```
05_llm_summariser_classifier/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py          # X-API-Key auth + LLM service DI
│   ├── endpoints/
│   │   ├── health.py            # GET /health
│   │   └── llm.py               # POST /summarise, /classify
│   ├── schemas/
│   │   ├── requests.py          # TextRequest
│   │   ├── responses.py         # HealthResponse
│   │   ├── llm.py               # SummariseResult, ClassifyResult
│   │   └── prompts.py           # System prompts + corrective hints
│   └── services/
│       ├── llm_service.py       # OpenAI wrapper + retry logic
│       └── json_parser.py       # JSON extraction from model output
├── tests/
│   ├── conftest.py
│   ├── endpoints/
│   ├── integration/
│   ├── schemas/
│   └── services/
├── .env.example
├── llm_summariser_assignment.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- OpenAI API key

---

## Setup

```bash
cd "01. Prerequisite Foundations/Assignments/05_llm_summariser_classifier"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
copy .env.example .env          # Windows
# cp .env.example .env          # macOS / Linux
```

Edit `.env`:

```env
LLM_SERVICE_API_KEY=demo-key
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

---

## Configuration

Environment variables are loaded from **this assignment's** `.env` file only (`05_llm_summariser_classifier/.env`). Copy `.env.example` to `.env` in the assignment folder before running.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes (live calls) | — | OpenAI API key for LLM calls |
| `LLM_SERVICE_API_KEY` | No | `demo-key` | Expected `X-API-Key` for POST endpoints |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | Chat model name |
| `llm_temperature` | — | `0.0` (hardcoded) | Model temperature |

---

## Run

```bash
fastapi dev app/main.py --port 8022
```

Alternative:

```bash
uvicorn app.main:app --reload --port 8022
```

- **Swagger UI:** http://127.0.0.1:8022/docs
- **Health check:** http://127.0.0.1:8022/health (no auth)

---

## Authentication

Both POST endpoints require:

```
X-API-Key: demo-key
```

Set `LLM_SERVICE_API_KEY` in `.env` to change the expected key. Validated via `secrets.compare_digest()` in `verify_api_key()`.

| Endpoint | Auth |
|----------|------|
| `GET /health` | None |
| `POST /summarise` | Required |
| `POST /classify` | Required |

---

## API reference

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | None | Liveness check |
| `POST` | `/summarise` | Yes | Summarise text (≤3 sentences) + word count |
| `POST` | `/classify` | Yes | Classify text into bug/feature/question/feedback |

### Request model

```python
class TextRequest(BaseModel):
    text: str = Field(min_length=1)
```

Both POST endpoints accept the same body:

```json
{"text": "Your input text here."}
```

### Response models

```python
class SummariseResult(BaseModel):
    summary: str
    word_count: int = Field(ge=0)

class ClassifyResult(BaseModel):
    category: str          # bug | feature | question | feedback
    confidence: float      # 0.0–1.0
    rationale: str
```

---

## Sample requests

Each example shows the **request body** (when applicable), **curl** command, and **response**.

> **Windows curl:** examples use `^` for line continuation. On macOS/Linux, use `\` instead.

---

### GET /health — Liveness check

**Auth:** None

**Request body:** None

```bash
curl http://127.0.0.1:8022/health
```

**Response `200`:**

```json
{"status": "ok"}
```

---

### POST /summarise — Summarise sprint planning notes

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": "During sprint planning the team reviewed blockers including payment gateway delays, iOS build failures, and limited QA capacity. The product owner proposed deferring the analytics dashboard and prioritising the checkout fix for Friday's release."
}
```

```bash
curl -X POST http://127.0.0.1:8022/summarise ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"During sprint planning the team reviewed blockers including payment gateway delays, iOS build failures, and limited QA capacity. The product owner proposed deferring the analytics dashboard and prioritising the checkout fix for Friday's release.\"}"
```

**Response `200`:**

```json
{
  "summary": "Team discussed sprint blockers and deferred analytics to prioritise checkout for Friday.",
  "word_count": 12
}
```

---

### POST /classify — Bug report

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": "The app crashes when I tap save on the settings page. This happens every time on Android 14."
}
```

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"The app crashes when I tap save on the settings page. This happens every time on Android 14.\"}"
```

**Response `200`:**

```json
{
  "category": "bug",
  "confidence": 0.93,
  "rationale": "Reports a reproducible crash with clear steps."
}
```

---

### POST /classify — Feature request

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": "Can we add a dark mode toggle in user settings?"
}
```

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Can we add a dark mode toggle in user settings?\"}"
```

**Response `200`:**

```json
{
  "category": "feature",
  "confidence": 0.91,
  "rationale": "User is requesting a new capability."
}
```

---

### POST /classify — Question

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": "Is there an export option for reports yet?"
}
```

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Is there an export option for reports yet?\"}"
```

**Response `200`:**

```json
{
  "category": "question",
  "confidence": 0.88,
  "rationale": "Asks whether a capability already exists."
}
```

---

### POST /classify — Feedback

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": "Love the new onboarding flow, much clearer than before."
}
```

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Love the new onboarding flow, much clearer than before.\"}"
```

**Response `200`:**

```json
{
  "category": "feedback",
  "confidence": 0.86,
  "rationale": "Positive comment about an existing experience."
}
```

---

### POST /classify — Missing API key (error)

**Auth:** None

**Request body:**

```json
{
  "text": "Can we add dark mode?"
}
```

```bash
curl -X POST http://127.0.0.1:8022/classify ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Can we add dark mode?\"}"
```

**Response `401`:**

```json
{"detail": "Invalid or missing API key."}
```

---

### POST /summarise — Empty text (validation error)

**Auth:** `X-API-Key: demo-key`

**Request body:**

```json
{
  "text": ""
}
```

```bash
curl -X POST http://127.0.0.1:8022/summarise ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"\"}"
```

**Response `422`:**

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "text"],
      "msg": "String should have at least 1 character",
      "input": ""
    }
  ]
}
```

---

## Structured prompts

Both endpoints instruct the model to return **JSON only** with explicit field definitions:

| Endpoint | JSON keys | Constraints |
|----------|-----------|-------------|
| `/summarise` | `summary`, `word_count` | Summary at most 3 sentences |
| `/classify` | `category`, `confidence`, `rationale` | `category` must be `bug`, `feature`, `question`, or `feedback` |

Responses are parsed and validated into Pydantic models before returning to the client.

---

## Failure handling

| Situation | HTTP status | Detail |
|-----------|-------------|--------|
| Success | 200 | Validated response body |
| Missing / wrong `X-API-Key` | 401 | `Invalid or missing API key.` |
| Empty `text` | 422 | Pydantic validation error |
| Missing `OPENAI_API_KEY` | 502 | `OpenAI API key is not configured.` |
| Invalid JSON after 1 retry | 502 | `LLM returned invalid JSON after retry.` |
| Invalid summary fields | 502 | `LLM returned invalid summary fields.` |
| Invalid category from model | 502 | `LLM returned an invalid classification.` |

### JSON retry flow

1. Call LLM with structured system prompt
2. Parse response as JSON
3. On parse failure → append bad response + corrective hint → **one retry**
4. Still invalid → **502** (no traceback leaked)

Corrective hints:

- Summarise: *"Return only JSON with keys summary and word_count."*
- Classify: *"Return only JSON. category must be exactly one of: bug, feature, question, feedback."*

**Note:** Validation failures (valid JSON but wrong category) are **not** retried — they return 502 immediately.

---

## Testing in Swagger UI

1. Open http://127.0.0.1:8022/docs
2. Expand `POST /summarise` or `POST /classify` → **Try it out**
3. Add header `X-API-Key: demo-key`
4. Paste a JSON body and click **Execute**

---

## Tests

```bash
pytest tests/ -v
```

LLM client is **mocked** — no network calls required. Tests cover:

- Unauthed POST → 401
- Empty text → 422
- Mocked summarise/classify return correct shape
- JSON retry logic (success on retry, 502 after two failures)
- Invalid category rejection → 502

---

## Submission checklist

- [ ] FastAPI app with `/health`, `/summarise`, `/classify`
- [ ] Structured JSON prompts parsed into Pydantic response models
- [ ] `X-API-Key` `Depends` dependency on both POST endpoints
- [ ] JSON-retry then 502 on persistent LLM failure; classify capped to 4 categories
- [ ] `TestClient` tests (LLM mocked) + README with run, auth, and 4 sample requests + `.env.example`

**Foundation pass criteria:** 30/50 overall, with at least **8/20** across Assignments 04–05.
