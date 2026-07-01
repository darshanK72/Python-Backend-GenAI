# 28 — Mounting a Flask app inside FastAPI
# Run: uvicorn 28_mount_flask:app --reload --port 8000
# FastAPI: http://127.0.0.1:8000/api/hello
# Flask:  http://127.0.0.1:8000/legacy/

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")
def legacy_home():
    return "Hello from legacy Flask app mounted at /legacy"


fastapi_app = FastAPI(title="Lesson 28 — Mount Flask")


@fastapi_app.get("/api/hello")
def api_hello():
    return {"message": "Hello from FastAPI"}


fastapi_app.mount("/legacy", WSGIMiddleware(flask_app))

app = fastapi_app
