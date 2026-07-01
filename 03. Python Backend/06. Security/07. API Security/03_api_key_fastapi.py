# 03 — API key in header (FastAPI dependency)
# Run: uvicorn 03_api_key_fastapi:app --port 8011
# Test: curl -H "X-API-Key: demo-key" http://127.0.0.1:8011/protected

import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI(title="API key demo")
VALID_KEY = os.getenv("LESSON_API_KEY", "demo-key")


def verify_api_key(x_api_key: str = Header(default="")):
    if not secrets.compare_digest(x_api_key, VALID_KEY):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key


@app.get("/protected")
def protected_route(_: str = Depends(verify_api_key)):
    return {"message": "authenticated request"}
