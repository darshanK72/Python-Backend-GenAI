# 02 — Golden signals for backends
# Run: python 02_golden_signals.py

SIGNALS = {
    "Latency": "How long requests take (p50, p95, p99)",
    "Traffic": "Requests per second",
    "Errors": "Rate of 5xx and failed jobs",
    "Saturation": "CPU, memory, queue depth, DB connections",
}

if __name__ == "__main__":
    print("Google SRE — four golden signals:\n")
    for name, detail in SIGNALS.items():
        print(f"  {name:12} {detail}")
