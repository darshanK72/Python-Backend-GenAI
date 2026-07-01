# 01 — logging module basics
# Run: python 01_logging_basics.py

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
log = logging.getLogger("api")

if __name__ == "__main__":
    log.debug("hidden unless DEBUG level")
    log.info("server started")
    log.warning("disk 80% full")
    log.error("failed to reach payment provider")
