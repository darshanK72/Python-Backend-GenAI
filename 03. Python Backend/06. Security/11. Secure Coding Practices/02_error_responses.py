# 02 — Safe error responses (no stack traces to clients)
# Run: python 02_error_responses.py

import logging

log = logging.getLogger("api")
logging.basicConfig(level=logging.ERROR)


def handle_error(exc: Exception, debug: bool = False) -> dict:
    log.exception("Unhandled error")
    if debug:
        return {"error": str(exc), "type": type(exc).__name__}
    return {"error": "Internal server error"}


if __name__ == "__main__":
    try:
        raise ValueError("database connection string invalid")
    except Exception as e:
        print("Production response:", handle_error(e, debug=False))
        print("Debug response:", handle_error(e, debug=True))
