# 02 — Capstone walkthrough (what each layer does)
# Run: python 02_capstone_walkthrough.py

LAYERS = [
    ("Transport", "HTTPS + reverse proxy in production"),
    ("Authentication", "X-API-Key header on every request"),
    ("Authorization", "Extend with user roles / note ownership"),
    ("Validation", "Pydantic rejects bad JSON payloads"),
    ("Rate limiting", "429 after too many requests per minute"),
    ("Logging", "Redact secrets; log errors server-side only"),
]

if __name__ == "__main__":
    print("Secure Notes API layers:\n")
    for name, detail in LAYERS:
        print(f"  {name:16} {detail}")
    print("\nStart server:")
    print("  uvicorn 01_secure_notes_api:app --port 8012")
