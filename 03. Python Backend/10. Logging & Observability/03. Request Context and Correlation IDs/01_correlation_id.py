# 01 — Correlation / request ID with contextvars
# Run: python 01_correlation_id.py

import logging
import uuid
from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar("request_id", default="-")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s rid=%(request_id)s %(levelname)s %(message)s",
)


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True


log = logging.getLogger("api")
log.addFilter(RequestIdFilter())


def handle_request():
    request_id_var.set(str(uuid.uuid4())[:8])
    log.info("processing request")
    log.info("calling database")


if __name__ == "__main__":
    handle_request()
