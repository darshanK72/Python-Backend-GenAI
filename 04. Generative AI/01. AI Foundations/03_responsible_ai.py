# 03 — Responsible AI checklist
# Run: python 03_responsible_ai.py

CHECKLIST = [
    "Disclose when content is AI-generated",
    "Avoid sending secrets/PII to third-party models",
    "Review outputs for hallucinations before production use",
    "Log and monitor prompts/responses (redact sensitive data)",
    "Prefer retrieval (RAG) over guessing facts",
]

if __name__ == "__main__":
    print("Responsible Gen AI practices:\n")
    for i, item in enumerate(CHECKLIST, 1):
        print(f"  {i}. {item}")
