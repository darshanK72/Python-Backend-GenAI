# 03 — WebSocket chat (broadcast to all clients)
# Run: python 03_websocket_chat_server.py
# Open multiple terminals with: python 03_websocket_chat_client.py YourName

import asyncio

try:
    import websockets
except ImportError:
    print("Install: pip install websockets")
    raise SystemExit(1)

HOST = "localhost"
PORT = 8766
clients: set = set()


async def chat_handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            outgoing = message  # format: "Name: hello"
            await asyncio.gather(
                *[client.send(outgoing) for client in clients],
                return_exceptions=True,
            )
    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(chat_handler, HOST, PORT):
        print(f"Chat server ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
