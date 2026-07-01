# 01 — Twelve-Factor App principles (backend focus)
# Run: python 01_twelve_factor.py

FACTORS = [
    ("I. Codebase", "One repo, many deploys"),
    ("II. Dependencies", "Explicit in requirements.txt / lock file"),
    ("III. Config", "Store in environment, not in code"),
    ("IV. Backing services", "Treat DB/Redis as attached resources"),
    ("V. Build, release, run", "Separate build image from runtime config"),
    ("VI. Processes", "Stateless app processes; state in DB/cache"),
    ("VII. Port binding", "App exports HTTP via a port (Uvicorn/Gunicorn)"),
    ("VIII. Concurrency", "Scale out with more worker processes"),
    ("IX. Disposability", "Fast startup, graceful shutdown"),
    ("X. Dev/prod parity", "Keep environments as similar as possible"),
    ("XI. Logs", "Treat logs as event streams (stdout)"),
    ("XII. Admin processes", "One-off jobs as separate commands"),
]

if __name__ == "__main__":
    print("Twelve-Factor App — backend highlights:\n")
    for name, detail in FACTORS:
        print(f"  {name:22} {detail}")
