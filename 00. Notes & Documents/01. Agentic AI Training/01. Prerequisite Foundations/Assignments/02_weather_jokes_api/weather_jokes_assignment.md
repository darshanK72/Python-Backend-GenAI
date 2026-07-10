# Assignment 02 — Weather & Jokes API Service

**Source:** MAS_TRAINING-000_Prerequisite_Foundations  
**Track:** FastAPI & Web Services  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · FastAPI · httpx/requests · Pydantic

---

## Pattern

FastAPI — typed endpoints, external API calls, Pydantic response models, error handling.

---

## Scenario

A team wants a single internal service that wraps a couple of noisy third-party APIs behind clean, documented, validated endpoints — so the rest of the team never has to handle raw upstream JSON or leaked API keys again. You are building that gateway service with FastAPI, the same framework the MAS program uses for its agent-to-agent work.

---

## What You Need to Build

A FastAPI application, `main.py`, exposing three endpoints. All responses are typed with Pydantic models. The upstream weather key is loaded from the environment, never hardcoded.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Returns `{"status": "ok"}` — a liveness check. |
| `GET` | `/weather?city={city}` | Calls the OpenWeather API for the city and returns a trimmed, typed response: `city`, `temp_c`, `conditions`. |
| `GET` | `/joke` | Calls JokeAPI and returns a typed response: `setup` and `delivery` (or a single-line joke normalised into the same shape). |

### Pydantic models

| Model | Fields |
|-------|--------|
| `WeatherResponse` | `city` (str), `temp_c` (float), `conditions` (str) |
| `JokeResponse` | `setup` (str), `delivery` (str) |

FastAPI must use these as `response_model` so the schema appears in `/docs`.

### Behaviours & constraints

- **Upstream errors:** If OpenWeather returns a 404 for an unknown city, your service returns HTTP **404** with a clear JSON `detail` — not a 500. If the upstream is unreachable, return **502** with a clear message.
- **Missing param:** A request to `/weather` with no `city` returns **422** (FastAPI validation) — demonstrate this in the README.
- **Secrets:** The OpenWeather API key is read from an environment variable (e.g. via a `.env` loaded with `os.environ` or `python-dotenv`). The key is never committed; `.env` is in `.gitignore` and a `.env.example` is provided.
- **Docs:** All three endpoints appear in the auto-generated `/docs` with correct response schemas.

### Sample requests to cover in README

| Request | Expected |
|---------|----------|
| `GET /weather?city=London` | 200 with temp and conditions |
| `GET /weather?city=NotARealCity` | 404 with clear detail |
| `GET /weather` (no city) | 422 validation error |
| `GET /joke` | 200 with setup/delivery |

### External APIs

| API | Usage | Key required |
|-----|-------|--------------|
| [OpenWeather](https://openweathermap.org/api) | `/weather` endpoint | Yes — free key |
| [JokeAPI](https://v2.jokeapi.dev/) | `/joke` endpoint | No |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Service Skeleton** | FastAPI app, virtual environment, `/health` endpoint, and Pydantic response models defined. | 30 min |
| **M2 — External API Integration** | Wire `/weather` and `/joke` to the upstream APIs via httpx/requests; map upstream JSON into your models. | 50 min |
| **M3 — Errors & Secrets** | Map upstream failures to correct status codes; load the key from the environment; add `.env.example`. | 40 min |
| **M4 — Testing & Docs** | Exercise all endpoints via `/docs`; README with the four sample requests and run command. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Structure & Correctness** | FastAPI app with all 3 endpoints; Pydantic `response_model`s used; runs with `fastapi dev` and appears in `/docs` | Endpoints work but no Pydantic models, or a framework other than FastAPI used (–1) | Not a working FastAPI app; endpoints missing |
| 2 | **Core Functionality** | `/weather` and `/joke` return correct trimmed, typed data from the live upstreams | One endpoint works; the other returns raw upstream JSON or wrong fields | Neither external endpoint returns correct data |
| 3 | **Error Handling & Robustness** | Unknown city → 404; unreachable upstream → 502; missing param → 422; all with clear detail | Some error paths handled; at least one returns a 500 / leaks a traceback | No error mapping; upstream failures crash the service |
| 4 | **End-to-End Run** | All four README sample requests behave exactly as specified | 3 of 4 behave correctly | Service crashes or core requests fail |
| 5 | **Documentation** | README with run command + 4 sample requests; `.env.example` present; key not committed | Runs; README thin or `.env.example` missing | No README; or API key committed to git (red flag) |

---

## Submission Checklist

- [ ] FastAPI app with `/health`, `/weather`, `/joke` and Pydantic response models
- [ ] API key loaded from environment; `.env` in `.gitignore`; `.env.example` committed
- [ ] README with run command and the four sample requests + responses
- [ ] All endpoints visible with correct schemas in `/docs`

---

## Pass context (foundation course)

Foundation pass criteria: **30/50 overall**, with at least **12/30** across Assignments 01–03.
