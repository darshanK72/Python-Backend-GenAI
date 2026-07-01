# 02 — Manual span demo (conceptual)
# Run: python 02_manual_span_demo.py

import time
import uuid


def trace_request():
    trace_id = str(uuid.uuid4())[:8]
    spans = []

    def span(name: str):
        start = time.perf_counter()

        def end():
            ms = int((time.perf_counter() - start) * 1000)
            spans.append({"trace_id": trace_id, "span": name, "duration_ms": ms})

        return end

    finish = span("http_handler")
    time.sleep(0.02)
    db_done = span("db_query")
    time.sleep(0.03)
    db_done()
    finish()
    return spans


if __name__ == "__main__":
    for s in trace_request():
        print(s)
