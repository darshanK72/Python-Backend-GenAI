# 24 — WebSockets
# Run: uvicorn 24_websockets:app --reload --port 8000
# Connect with a WebSocket client to ws://127.0.0.1:8000/ws/chat
# Or use the "Try it" section in /docs for /ws/echo

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Lesson 24 — WebSockets")


@app.websocket("/ws/echo")
async def echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        pass


@app.websocket("/ws/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to the chat room!")
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f"User said: {message}")
    except WebSocketDisconnect:
        await websocket.close()
