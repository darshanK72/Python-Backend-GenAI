# Assignment 05 — LLM Summariser & Classifier Service

**Source:** MAS_TRAINING-000_Prerequisite_Foundations  
**Track:** GenAI + FastAPI  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · FastAPI · OpenAI (or equiv) · Pydantic · pytest

---

## Pattern

GenAI + FastAPI — LLM-backed endpoints, structured output, auth, prompt design, tests.

---

## Scenario

This capstone ties the three tracks together. A team wants an internal service that takes raw text and returns a clean summary and a category tag, behind a secured endpoint — the exact shape of an MAS agent tool. You are combining everything: a FastAPI service (Tracks 1–2) wrapping LLM calls with well-engineered, structured prompts (Track 3), with auth and tests.

---

## What You Need to Build

A FastAPI application exposing two LLM-backed endpoints plus a health check. Requests require an API-key header (reuse the dependency pattern from Assignment 03). The model is called with structured prompts that return JSON, which is validated into Pydantic models before responding. The LLM key is loaded from the environment.

### Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | None | Liveness check. |
| `POST` | `/summarise` | Required | Body: `{text: str}`. Returns `{summary: str, word_count: int}` — summary is 3 sentences max. |
| `POST` | `/classify` | Required | Body: `{text: str}`. Returns `{category: one of bug/feature/question/feedback, confidence: float, rationale: str}`. |

### Behaviours & constraints

- **Structured prompts:** Both endpoints instruct the model to return JSON only, with explicit fields and (for classify) the allowed category values. The response is parsed and validated into a Pydantic model before being returned.
- **LLM failure handling:** If the model returns invalid JSON, retry once with a corrective instruction; if it still fails, return HTTP **502** with a clear detail — do not return a 500 traceback.
- **Auth:** Both POST endpoints are guarded by an `X-API-Key` `Depends` dependency; missing/wrong key → **401**.
- **Validation:** Empty text → **422** via Pydantic. `classify` must only ever return one of the four allowed categories — reject/repair anything else.
- **Secrets:** LLM key from environment; never committed; `.env.example` provided.
- **Tests:** pytest tests with `TestClient`: unauthed call → 401; empty text → 422; a mocked or live summarise returns the right shape. (Mocking the LLM call is encouraged so tests don't depend on the network.)

### Sample requests to cover in README

| Request | Expected |
|---------|----------|
| `POST /summarise` with a long paragraph | **200** with a ≤3-sentence summary and `word_count` |
| `POST /classify` with a bug report | **200** with `category` `bug` and a `confidence` |
| `POST /classify` with no key | **401** |
| `POST /summarise` with empty text | **422** |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Service & Models** | FastAPI app, `/health`, Pydantic request/response models, and the env-loaded LLM client. | 30 min |
| **M2 — LLM Endpoints** | Implement `/summarise` and `/classify` with structured JSON prompts parsed into the response models. | 50 min |
| **M3 — Auth & Failure Handling** | Add the `X-API-Key` dependency to both POSTs; add JSON-retry and 502 mapping; cap categories to the allowed set. | 40 min |
| **M4 — Tests & Docs** | Write the `TestClient` tests (mock the LLM); README with run command, auth, and the four sample requests. | 40 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Structure & Correctness** | FastAPI app; both LLM endpoints return Pydantic-validated structured output; key from environment; appears in `/docs` | Endpoints work but return raw model text instead of validated models, or key hardcoded (–1) | Not a working FastAPI app; LLM calls absent or broken |
| 2 | **Core Functionality (Prompts + Auth)** | Structured prompts yield valid JSON for both tasks; classify restricted to 4 categories; both POSTs auth-guarded via `Depends` | One endpoint solid, the other unreliable; or auth inline rather than a dependency | Prompts unstructured; no auth; classify returns arbitrary categories |
| 3 | **Robustness (LLM + validation)** | Invalid JSON → one corrective retry then 502; empty text → 422; bad category repaired/rejected; no tracebacks | Some handled; one path returns a 500 or leaks a traceback | No failure handling; bad model output crashes the endpoint |
| 4 | **End-to-End Run** | All four README sample requests behave exactly as specified | 3 of 4 behave correctly | Service crashes or core requests fail |
| 5 | **Documentation & Tests** | `TestClient` tests pass (LLM mocked); README with run + auth + 4 samples; `.env.example` committed | Runs; tests partial or README thin | No tests; no README; or key committed (red flag) |

---

## Submission Checklist

- [ ] FastAPI app with `/health`, `/summarise`, `/classify`
- [ ] Structured JSON prompts parsed into Pydantic response models
- [ ] `X-API-Key` `Depends` dependency on both POST endpoints
- [ ] JSON-retry then 502 on persistent LLM failure; classify capped to 4 categories
- [ ] `TestClient` tests (LLM mocked) + README with run, auth, and 4 sample requests + `.env.example`

---

## Pass context (foundation course)

Foundation pass criteria: **30/50 overall**, with at least **8/20** across Assignments 04–05.
