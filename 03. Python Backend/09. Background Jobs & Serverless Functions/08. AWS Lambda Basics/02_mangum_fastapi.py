# 02 — FastAPI on Lambda with Mangum
# Run: python 02_mangum_fastapi.py
# Install: pip install mangum

try:
    from mangum import Mangum
except ImportError:
    print("Install: pip install mangum")
    raise SystemExit(1)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"runtime": "lambda-ready"}


handler = Mangum(app)

if __name__ == "__main__":
    print("Mangum wraps ASGI for AWS Lambda + API Gateway.")
    print("Deploy handler = 02_mangum_fastapi.handler")
