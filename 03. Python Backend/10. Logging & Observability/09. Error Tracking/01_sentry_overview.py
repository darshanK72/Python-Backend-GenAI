# 01 — Sentry error tracking overview
# Run: python 01_sentry_overview.py

SETUP = '''
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FastApiIntegration()],
    traces_sample_rate=0.1,
    environment=os.getenv("APP_STAGE", "development"),
)
'''

if __name__ == "__main__":
    print("Sentry captures unhandled exceptions with stack traces.")
    print("Install: pip install sentry-sdk")
    print("\nFastAPI setup:\n", SETUP.strip())
