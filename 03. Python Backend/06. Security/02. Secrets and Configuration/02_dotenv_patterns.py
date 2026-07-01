# 02 — dotenv patterns for dev vs production
# Run: python 02_dotenv_patterns.py

import os
from pathlib import Path

ENV = os.getenv("APP_ENV", "development")


def load_config() -> dict:
    """Dev: .env file. Production: real env vars from host/CI."""
    try:
        from dotenv import load_dotenv

        if ENV == "development":
            root = Path(__file__).resolve().parents[3]
            load_dotenv(root / ".env")
    except ImportError:
        pass

    return {
        "env": ENV,
        "debug": os.getenv("DEBUG", "false").lower() == "true",
        "database_url": os.getenv("DATABASE_URL", "sqlite:///local.db"),
        "secret_key": os.getenv("SECRET_KEY", ""),
    }


if __name__ == "__main__":
    cfg = load_config()
    print("APP_ENV:", cfg["env"])
    print("DEBUG:", cfg["debug"])
    print("DATABASE_URL set:", bool(cfg["database_url"]))
    print("SECRET_KEY set:", bool(cfg["secret_key"]))
    print("\nProduction: inject secrets via platform (Docker secrets, K8s, CI vars).")
