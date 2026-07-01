# 02 — Capture exception with context
# Run: python 02_exception_context.py

import logging

log = logging.getLogger("errors")
logging.basicConfig(level=logging.ERROR)


def process_order(order_id: int):
    try:
        raise ValueError(f"payment failed for order {order_id}")
    except Exception:
        log.exception("order_processing_failed", extra={"order_id": order_id})


if __name__ == "__main__":
    process_order(1001)
    print("\nIn production, same exception also goes to Sentry/Datadog.")
