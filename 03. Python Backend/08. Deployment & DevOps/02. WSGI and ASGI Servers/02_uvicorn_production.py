# 02 — Uvicorn production options
# Run: python 02_uvicorn_production.py

COMMANDS = [
    "# Development (auto-reload)",
    "uvicorn main:app --reload --host 127.0.0.1 --port 8000",
    "",
    "# Production (single process)",
    "uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1",
    "",
    "# Production (multiple workers — Linux/macOS)",
    "uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4",
    "",
    "# Behind reverse proxy — bind locally only",
    "uvicorn main:app --host 127.0.0.1 --port 8000 --proxy-headers",
]

if __name__ == "__main__":
    print("Uvicorn deployment commands:\n")
    for line in COMMANDS:
        print(line)
