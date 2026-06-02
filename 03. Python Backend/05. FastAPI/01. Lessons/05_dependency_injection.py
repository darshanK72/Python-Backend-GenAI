# 05 — Dependencies (shared logic)
# Run: uvicorn 05_dependency_injection:app --reload --port 8000

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI(title="Lesson 05")


def verify_api_key(x_api_key: str = Header(default="")):
    if x_api_key != "secret-demo-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key


@app.get("/protected")
def protected_route(key: str = Depends(verify_api_key)):
    return {"message": "Access granted", "key_used": key}
