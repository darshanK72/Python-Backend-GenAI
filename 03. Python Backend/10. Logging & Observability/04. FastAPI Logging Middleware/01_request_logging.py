# 01 — FastAPI request logging middleware
# Run: uvicorn app:app --port 8021
# Test: curl -H "X-Request-ID: demo-1" http://127.0.0.1:8021/notes

if __name__ == "__main__":
    print("Start server:")
    print("  uvicorn app:app --port 8021")
    print("Watch structured request start/end lines in terminal.")
