# Lesson 29 — Deploying FastAPI to Production

**Topics:** Development vs production, Uvicorn/Gunicorn, reverse proxy, environment config, containers, checklist

**Practice project:** `../02. Notes API/main.py`

**Deeper coverage:** `08. Deployment & DevOps/` in this repo (Docker, CI/CD, health checks, TLS)

---

## Development vs production

During development you want **fast feedback**. In production you want **stability, security, and throughput**.

| | Development | Production |
|---|-------------|------------|
| Server | `uvicorn main:app --reload` | Multiple workers, no `--reload` |
| HTTPS | Often HTTP on localhost | TLS at reverse proxy or load balancer |
| Secrets | `.env` file (gitignored) | Environment variables / secret manager |
| Debug | Verbose logs, tracebacks OK | Structured logs, safe error messages |
| Static files | Served by FastAPI | Often CDN or reverse proxy |

**Never use `--reload` in production.** It watches files and restarts the process — useful locally, wasteful and risky in prod.

---

## Running Uvicorn

### Local development

```bash
uvicorn main:app --reload --port 8000
```

- `main:app` — Python module `main.py`, variable `app`
- `--reload` — restart on file changes (dev only)
- `--host 0.0.0.0` — listen on all interfaces (needed in Docker/VM)

### Production (single machine)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Workers** are separate processes. Rule of thumb: `(2 × CPU cores) + 1`, then tune with load testing.

Each worker is a full Python process with its own memory. In-memory caches (dicts, global variables) are **not shared** across workers — use Redis or a database for shared state.

---

## Gunicorn + Uvicorn workers

Many teams run **Gunicorn** as the process manager and **Uvicorn** as the worker class:

```bash
pip install gunicorn uvicorn
gunicorn main:app -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000
```

| Component | Role |
|-----------|------|
| Gunicorn | Spawns/manages worker processes, handles signals |
| UvicornWorker | Runs the ASGI app inside each worker |

Gunicorn gives mature process management (graceful restarts, worker lifecycle). See `08. Deployment & DevOps/02. WSGI and ASGI Servers/` for comparisons.

---

## Reverse proxy (Nginx / Caddy)

Do **not** expose Uvicorn directly to the public internet. Put a **reverse proxy** in front:

```
Internet ──HTTPS──► Nginx / Caddy ──HTTP──► Uvicorn (127.0.0.1:8000)
```

The proxy handles:

- **TLS termination** — certificates and HTTPS
- **HTTP/2** — optional performance benefit
- **Static files** — `/static/` without hitting Python
- **Rate limiting** — basic protection
- **Timeouts and buffering** — protect app from slow clients

Example Nginx location block (simplified):

```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

FastAPI should trust `X-Forwarded-*` headers only when behind a known proxy. See `08. Deployment & DevOps/05. Reverse Proxy and TLS/`.

---

## Environment and secrets

Store secrets **outside** source code:

- `DATABASE_URL`
- `SECRET_KEY` / JWT signing keys
- Third-party API keys

**Development:** copy `config.example.env` to `.env` at the repo root and load with `python-dotenv` or **pydantic-settings**:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    debug: bool = False

    model_config = {"env_file": ".env"}
```

**Production:** inject variables via your platform (Kubernetes secrets, AWS Parameter Store, Azure Key Vault, etc.). Never commit `.env` to git.

See `06. Security/02. Secrets and Configuration/` and `08. Deployment & DevOps/01. Twelve-Factor and Environment/`.

---

## Application settings for production

```python
app = FastAPI(
    title="My API",
    docs_url="/docs" if settings.debug else None,  # hide docs in prod
    redoc_url=None,
)
```

Production checklist for the app itself:

- [ ] `DEBUG = False` (or equivalent)
- [ ] Restrict **CORS** to real front-end origins (lesson 19 — avoid `allow_origins=["*"]` with credentials)
- [ ] Structured **logging** (JSON logs, correlation IDs) — `10. Logging & Observability/`
- [ ] **Health endpoints** — `GET /health` for load balancers
- [ ] **Database** — connection pooling, migrations (Alembic)
- [ ] **Auth** — API keys, JWT, or OAuth as appropriate — `06. Security/04. Authentication/`

---

## Docker

A minimal `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t my-fastapi-api .
docker run -p 8000:8000 --env-file .env my-fastapi-api
```

For multi-service stacks (API + Postgres + Redis), use **Docker Compose**. See `08. Deployment & DevOps/03. Docker Basics/` and `04. Docker Compose/`.

Deploy to **Kubernetes**, **AWS ECS**, **Google Cloud Run**, or **Azure Container Apps** with:

- Liveness probe → `GET /health`
- Readiness probe → `GET /ready` (checks DB connectivity)
- Resource limits (CPU/memory)

---

## Graceful shutdown

When a container or process receives `SIGTERM`, Uvicorn should finish in-flight requests before exiting. Use **lifespan** handlers (lesson 25) to close DB pools and flush connections:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: open pools, warm cache
    yield
    # shutdown: close clients, drain queues
```

See `08. Deployment & DevOps/10. Health Checks and Graceful Shutdown/`.

---

## CI/CD pipeline (overview)

A typical pipeline:

1. **Lint / type check** — ruff, mypy
2. **Test** — pytest with `TestClient` (`07. Testing/07. FastAPI Testing/`)
3. **Security scan** — bandit, pip-audit (`06. Security/12. Security Scanning/`)
4. **Build image** — Docker
5. **Deploy** — rolling update to staging, then production

See `08. Deployment & DevOps/09. CI CD Pipelines/`.

---

## Production checklist

### Server and network

- [ ] Uvicorn/Gunicorn with multiple workers (no `--reload`)
- [ ] Reverse proxy with HTTPS
- [ ] Firewall — only proxy ports public; app on localhost or private network

### Application

- [ ] Secrets in environment variables
- [ ] CORS restricted to known origins
- [ ] Interactive docs disabled or protected in production
- [ ] Rate limiting on public endpoints
- [ ] Input validation (Pydantic — already default in FastAPI)

### Data

- [ ] Managed database with backups
- [ ] Connection pooling configured
- [ ] Migrations applied (Alembic)

### Observability

- [ ] Structured logging
- [ ] Health and readiness endpoints
- [ ] Error tracking (e.g. Sentry) — `10. Logging & Observability/09. Error Tracking/`
- [ ] Metrics (Prometheus) — optional but recommended at scale

### Security

- [ ] Dependencies pinned and scanned
- [ ] Authentication on sensitive routes
- [ ] Security headers via proxy or middleware — `06. Security/03. Transport Security/`

---

## Capstone: Notes API

Apply everything in the practice project:

```bash
cd "../02. Notes API"
uvicorn main:app --reload --port 8000
```

Then review `08. Deployment & DevOps/11. Deployment Capstone/` for a Dockerized deploy walkthrough.

---

## Summary

| Layer | Tool |
|-------|------|
| App | FastAPI |
| ASGI server | Uvicorn (or Gunicorn + UvicornWorker) |
| TLS / static / routing | Nginx or Caddy |
| Config | Environment variables + pydantic-settings |
| Packaging | Docker |
| Orchestration | K8s, ECS, Cloud Run, etc. |

Deploy FastAPI with **Uvicorn + HTTPS reverse proxy + env-based config**. Treat lesson 29 as the map; use `08. Deployment & DevOps/` for hands-on deployment lessons.
