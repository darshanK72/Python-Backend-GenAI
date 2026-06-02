# 05 — logging (better than print for apps)
# Run: python 05_logging.py

import logging

# --- 1. Basic config ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

logging.debug("Debug message (hidden at INFO level)")
logging.info("App started")
logging.warning("Low disk space")
logging.error("Failed to connect")

# --- 2. Logger with name ---
logger = logging.getLogger("payments")
logger.info("Payment processed: order 42")

# --- 3. Log exception ---
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Calculation failed")
