# Flask app with request logging
# Run: python app.py

import logging
import time
import uuid

from flask import Flask, g, request

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("flask")

app = Flask(__name__)


@app.before_request
def start_timer():
    g.request_id = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
    g.start = time.perf_counter()


@app.after_request
def log_response(response):
    ms = int((time.perf_counter() - g.start) * 1000)
    log.info(
        "rid=%s %s %s -> %s %sms",
        g.request_id,
        request.method,
        request.path,
        response.status_code,
        ms,
    )
    response.headers["X-Request-ID"] = g.request_id
    return response


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(port=5021, debug=False)
