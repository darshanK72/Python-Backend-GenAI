# 03 — Log levels and when to use them
# Run: python 03_log_levels.py

LEVELS = {
    "DEBUG": "Detailed diagnostic (dev only)",
    "INFO": "Normal operations (startup, request served)",
    "WARNING": "Recoverable issue (retry, deprecated API)",
    "ERROR": "Failed operation (needs attention)",
    "CRITICAL": "System unusable",
}

if __name__ == "__main__":
    print("Python logging levels:\n")
    for level, use in LEVELS.items():
        print(f"  {level:8} {use}")
