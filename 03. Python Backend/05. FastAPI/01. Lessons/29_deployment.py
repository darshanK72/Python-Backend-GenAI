# 29 — Deployment (read-only)
# Run: python 29_deployment.py

# --- Development ---
#   uvicorn 02_hello:app --reload --port 8000
# --reload is for local dev only (restarts on file changes).

# --- Production ASGI server ---
# Run multiple workers (processes) behind a reverse proxy:
#   uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
# Or use Gunicorn with Uvicorn workers:
#   gunicorn main:app -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000

# --- Reverse proxy (Nginx / Caddy) ---
# Terminate TLS (HTTPS) at the proxy and forward HTTP to Uvicorn.
# Set proxy headers and timeouts; serve static files at the edge when possible.

# --- Environment ---
# Store secrets in env vars (DATABASE_URL, API_KEYS), not in code.
# Use pydantic-settings or python-dotenv to load .env in dev.

# --- Containers ---
# Dockerfile: install deps, COPY app, CMD uvicorn main:app --host 0.0.0.0 --port 8000
# Run behind Kubernetes / ECS / Cloud Run with health checks on GET /health.

# --- Checklist ---
# [ ] DEBUG off, structured logging
# [ ] CORS restricted to real front-end origins
# [ ] DB connection pooling, migrations (Alembic)
# [ ] Rate limiting / auth for public APIs

if __name__ == "__main__":
    print("Deploy FastAPI with Uvicorn + HTTPS reverse proxy + env-based config.")
    print("Practice project: see ../02. Notes API/main.py")
