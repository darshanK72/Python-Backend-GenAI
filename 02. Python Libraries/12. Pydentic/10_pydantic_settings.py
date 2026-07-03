# 10 — pydantic-settings (typed environment variables)
# Run: python 10_pydantic_settings.py
# Install: pip install pydantic-settings

from pathlib import Path

try:
    from pydantic import Field
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    print("Install: pip install pydantic-settings")
    raise SystemExit(1)

# --- 1. Demo .env file (removed at end) ---
env_path = Path(".env.pydantic_demo")
env_path.write_text(
    "APP_NAME=Learning Pydantic\n"
    "DEBUG=true\n"
    "MAX_UPLOAD_MB=25\n",
    encoding="utf-8",
)


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.pydantic_demo",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Default App"
    debug: bool = False
    max_upload_mb: int = Field(default=10, ge=1, le=500)


settings = AppSettings()
print("app_name:", settings.app_name)
print("debug:", settings.debug)
print("max_upload_mb:", settings.max_upload_mb)

env_path.unlink()
print("removed .env.pydantic_demo")

# Real projects: load from .env at repo root; never commit secrets.
