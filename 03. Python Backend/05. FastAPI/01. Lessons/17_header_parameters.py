# 17 — Header parameters
# Run: uvicorn 17_header_parameters:app --reload --port 8000
# GET /items  with header  X-Token: my-token

from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Lesson 17 — Header Parameters")


@app.get("/items")
def list_items(x_token: str = Header(alias="X-Token")):
    if x_token != "my-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"items": ["book", "pen"]}


@app.get("/agent")
def read_user_agent(user_agent: str | None = Header(default=None)):
    return {"user_agent": user_agent}
