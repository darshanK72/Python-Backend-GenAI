# 01 — Production security checklist
# Run: python 01_production_checklist.py

import os

CHECKLIST = [
    ("DEBUG is False", lambda: os.getenv("DEBUG", "false").lower() != "true"),
    ("SECRET_KEY is set", lambda: bool(os.getenv("SECRET_KEY"))),
    ("HTTPS enforced", lambda: os.getenv("FORCE_HTTPS", "false").lower() == "true"),
    ("CORS origins restricted", lambda: os.getenv("CORS_ALLOW_ALL", "true").lower() != "true"),
]


if __name__ == "__main__":
    print("Production security checklist:\n")
    for label, check in CHECKLIST:
        status = "PASS" if check() else "WARN"
        print(f"  [{status}] {label}")
    print("\nSet env vars in deployment platform; never ship with DEBUG=True.")
