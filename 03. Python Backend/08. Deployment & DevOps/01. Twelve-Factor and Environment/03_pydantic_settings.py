# 03 — Typed settings with pydantic-settings
# Run: python 03_pydantic_settings.py
# Install: pip install pydantic-settings

import os

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("Install: pip install pydantic-settings")
    raise SystemExit(1)


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Notes API"
    app_stage: str = "development"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "change-me"


if __name__ == "__main__":
    settings = AppSettings()
    print("app_name:", settings.app_name)
    print("app_stage:", settings.app_stage)
    print("debug:", settings.debug)
    print("database_url:", settings.database_url)
    print("SECRET_KEY set:", settings.secret_key != "change-me" or bool(os.getenv("SECRET_KEY")))
