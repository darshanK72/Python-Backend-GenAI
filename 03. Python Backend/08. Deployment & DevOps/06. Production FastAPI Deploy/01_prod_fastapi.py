# 01 — FastAPI production settings
# Run: python 01_prod_fastapi.py

import os

if __name__ == "__main__":
    print("Production FastAPI checklist:\n")
    items = [
        "DEBUG=false, hide /docs in production",
        "Set explicit CORS allow_origins",
        "Use multiple Uvicorn workers or Gunicorn+UvicornWorker",
        "Bind 127.0.0.1 behind reverse proxy",
        "Load SECRET_KEY and DB URLs from environment",
        "Expose GET /health for load balancer",
    ]
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    print("\nRun app in this folder:")
    print("  uvicorn app:app --host 127.0.0.1 --port 8000")
    print("Current DEBUG env:", os.getenv("DEBUG", "(not set)"))
