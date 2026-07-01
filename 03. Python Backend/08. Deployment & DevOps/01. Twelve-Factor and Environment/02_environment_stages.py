# 02 — Environment stages (dev, staging, production)
# Run: python 02_environment_stages.py

import os

STAGE = os.getenv("APP_STAGE", "development")

SETTINGS = {
    "development": {"debug": True, "log_level": "DEBUG", "reload": True},
    "staging": {"debug": False, "log_level": "INFO", "reload": False},
    "production": {"debug": False, "log_level": "WARNING", "reload": False},
}


def current_settings() -> dict:
    return SETTINGS.get(STAGE, SETTINGS["development"])


if __name__ == "__main__":
    cfg = current_settings()
    print(f"APP_STAGE={STAGE}")
    print("Settings:", cfg)
    print("\nSet APP_STAGE=staging or production in deployment platform.")
