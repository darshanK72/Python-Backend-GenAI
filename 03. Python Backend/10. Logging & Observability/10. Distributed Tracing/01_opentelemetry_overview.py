# 01 — OpenTelemetry tracing overview
# Run: python 01_opentelemetry_overview.py

if __name__ == "__main__":
    print("Distributed tracing follows one request across services.")
    print("Components:")
    print("  Trace  — entire request journey")
    print("  Span   — one operation (HTTP call, DB query)")
    print("  Context — trace_id propagated in headers")
    print("\nInstall: pip install opentelemetry-api opentelemetry-sdk")
    print("Export to Jaeger, Grafana Tempo, or cloud APM.")
