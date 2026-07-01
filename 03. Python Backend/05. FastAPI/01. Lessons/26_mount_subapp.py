# 26 — Mounting a sub-application
# Run: uvicorn 26_mount_subapp:app --reload --port 8000
# Main app:  http://127.0.0.1:8000/
# Sub app:   http://127.0.0.1:8000/v2/

from fastapi import FastAPI

main_app = FastAPI(title="Lesson 26 — Main App")

sub_app = FastAPI(title="API v2", docs_url="/docs", openapi_url="/openapi.json")


@main_app.get("/")
def root():
    return {"app": "main", "hint": "Try /v2/ and /v2/docs"}


@sub_app.get("/")
def v2_root():
    return {"app": "v2", "version": "2.0"}


@sub_app.get("/health")
def v2_health():
    return {"status": "ok"}


main_app.mount("/v2", sub_app)

# uvicorn expects `app` — expose the main application
app = main_app
