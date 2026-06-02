# FastAPI

Placeholder for FastAPI learning projects.

## Getting started (when ready)

```bash
pip install fastapi "uvicorn[standard]"
```

Example minimal app (`main.py`):

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

Run: `uvicorn main:app --reload`

Suggested first project: **CRUD API** for notes or bookmarks with Pydantic models and optional SQLAlchemy.
