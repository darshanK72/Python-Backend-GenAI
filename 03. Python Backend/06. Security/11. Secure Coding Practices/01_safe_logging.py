# 01 — Safe logging (never log secrets or PII)
# Run: python 01_safe_logging.py

import logging
import re

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("app")

SENSITIVE_PATTERNS = [
    (re.compile(r"sk-[a-zA-Z0-9]{10,}"), "sk-***"),
    (re.compile(r"password=\S+"), "password=***"),
    (re.compile(r"\b\d{16}\b"), "****-card-redacted****"),
]


def redact(message: str) -> str:
    redacted = message
    for pattern, replacement in SENSITIVE_PATTERNS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def safe_log_info(message: str) -> None:
    log.info(redact(message))


if __name__ == "__main__":
    safe_log_info("User login ok for alice@example.com")
    safe_log_info("Using API key sk-live-abcdefghijklmnop in request")
    safe_log_info("payment card 4111111111111111 declined")
