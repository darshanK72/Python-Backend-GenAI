# 03 — Secrets hygiene (what never belongs in git)
# Run: python 03_never_commit_secrets.py

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
GITIGNORE = REPO_ROOT / ".gitignore"
EXAMPLE_ENV = REPO_ROOT / "config.example.env"

NEVER_COMMIT = [
    ".env",
    "*.pem",
    "*.key",
    "credentials.json",
    "id_rsa",
]

if __name__ == "__main__":
    print("Never commit real secrets. Use placeholders in example files.\n")
    print("Bad:")
    print('  API_KEY = "sk-live-abc123"')
    print("Good:")
    print('  API_KEY = os.getenv("API_KEY")')
    print("\nChecklist:")
    for name in NEVER_COMMIT:
        print(f"  - block {name} in .gitignore")

    if GITIGNORE.exists():
        text = GITIGNORE.read_text(encoding="utf-8", errors="ignore")
        print("\n.gitignore mentions .env:", ".env" in text)
    if EXAMPLE_ENV.exists():
        print("config.example.env exists:", EXAMPLE_ENV.name)
