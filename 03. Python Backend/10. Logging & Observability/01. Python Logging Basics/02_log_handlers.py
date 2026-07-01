# 02 — Handlers: console vs file
# Run: python 02_log_handlers.py

import logging
from pathlib import Path

LOG_FILE = Path(__file__).with_name("lesson.log")

log = logging.getLogger("handlers_demo")
log.setLevel(logging.INFO)
log.handlers.clear()

console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))

log.addHandler(console)
log.addHandler(file_handler)

if __name__ == "__main__":
    log.info("written to console and file")
    print(f"Log file: {LOG_FILE}")
