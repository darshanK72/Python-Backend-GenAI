# 02 — WebSocket client
# Run: python 02_websocket_client.py  (start 01_websocket_server.py first)

import asyncio

try:
    import websockets
except ImportError:
    print("Install: pip install websockets")
    raise SystemExit(1)

URI = "ws://localhost:8765"


async def main():
    async with websockets.connect(URI) as ws:
        await ws.send("Hello WebSocket")
        reply = await ws.recv()
        print("Sent: Hello WebSocket")
        print("Received:", reply)


if __name__ == "__main__":
    asyncio.run(main())
