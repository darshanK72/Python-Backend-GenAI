# 16 — Cookie parameters
# Run: uvicorn 16_cookie_parameters:app --reload --port 8000
# GET /login sets a cookie; GET /dashboard reads it

from fastapi import Cookie, FastAPI, Response

app = FastAPI(title="Lesson 16 — Cookies")


@app.get("/login")
def login(response: Response):
    response.set_cookie(key="session_id", value="demo-session-123", httponly=True)
    return {"message": "Logged in — check cookies in browser dev tools"}


@app.get("/dashboard")
def dashboard(session_id: str | None = Cookie(default=None)):
    if not session_id:
        return {"error": "Not logged in"}
    return {"session_id": session_id, "page": "dashboard"}
