# 01 — WebSocket server
# Run: python 01_websocket_server.py
# Then: python 02_websocket_client.py
# Install: pip install websockets

import asyncio

try:
    import websockets
except ImportError:
    print("Install: pip install websockets")
    raise SystemExit(1)

HOST = "localhost"
PORT = 8765


async def echo_handler(websocket):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")


async def main():
    async with websockets.serve(echo_handler, HOST, PORT):
        print(f"WebSocket server ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
