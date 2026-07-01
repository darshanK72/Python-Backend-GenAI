# 02 — Probe checklist for observability
# Run: python 02_probe_checklist.py

CHECKLIST = [
    "Liveness checks process only — not external DB",
    "Readiness checks DB/cache/message broker",
    "Log probe failures with reason",
    "Expose build version/git sha at /version (optional)",
]

if __name__ == "__main__":
    for i, item in enumerate(CHECKLIST, 1):
        print(f"  {i}. {item}")
