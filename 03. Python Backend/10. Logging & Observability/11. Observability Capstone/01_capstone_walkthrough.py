# 01 — Observability capstone walkthrough
# Run: python 01_capstone_walkthrough.py

if __name__ == "__main__":
    print("Three pillars in one API:")
    print("  Logs    — request lines with correlation id")
    print("  Metrics — GET /metrics (Prometheus)")
    print("  Traces  — add OpenTelemetry in production")
    print("\nStart:")
    print("  uvicorn app:app --port 8024")
    print("  curl http://127.0.0.1:8024/health")
    print("  curl http://127.0.0.1:8024/metrics")
