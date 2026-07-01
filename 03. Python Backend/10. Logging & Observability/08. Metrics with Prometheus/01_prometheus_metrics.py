# 01 — Prometheus metrics with prometheus_client
# Run: python 01_prometheus_metrics.py
# Then: curl http://127.0.0.1:9100/metrics
# Install: pip install prometheus-client

try:
    from prometheus_client import Counter, Histogram, start_http_server
except ImportError:
    print("Install: pip install prometheus-client")
    raise SystemExit(1)

import time

REQUESTS = Counter("api_requests_total", "Total API requests", ["method", "endpoint"])
LATENCY = Histogram("api_request_duration_seconds", "Request latency")


def handle_request(method: str, endpoint: str):
    start = time.perf_counter()
    REQUESTS.labels(method=method, endpoint=endpoint).inc()
    time.sleep(0.05)
    LATENCY.observe(time.perf_counter() - start)


if __name__ == "__main__":
    start_http_server(9100)
    print("Metrics on http://127.0.0.1:9100/metrics")
    handle_request("GET", "/notes")
    handle_request("POST", "/notes")
    input("Press Enter to stop...")
