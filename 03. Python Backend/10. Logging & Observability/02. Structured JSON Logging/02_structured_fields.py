# 02 — Structured fields in log records
# Run: python 02_structured_fields.py

import json
import logging


def log_event(logger: logging.Logger, event: str, **fields):
    logger.info(json.dumps({"event": event, **fields}))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    log = logging.getLogger("events")
    log_event(log, "order_created", order_id=1001, user_id=42, amount=49.99)
