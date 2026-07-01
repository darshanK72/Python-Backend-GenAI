# 03 — WebSocket chat client
# Run: python 03_websocket_chat_client.py Asha

import asyncio
import sys

try:
    import websockets
except ImportError:
    print("Install: pip install websockets")
    raise SystemExit(1)

URI = "ws://localhost:8766"
NAME = sys.argv[1] if len(sys.argv) > 1 else "Guest"


async def main():
    async with websockets.connect(URI) as ws:
        print(f"Connected as {NAME}. Type messages (Ctrl+C to quit).")
        await ws.send(f"{NAME} joined the chat")

        async def reader():
            async for message in ws:
                print(message)

        async def writer():
            loop = asyncio.get_running_loop()
            while True:
                text = await loop.run_in_executor(None, sys.stdin.readline)
                if not text:
                    continue
                await ws.send(f"{NAME}: {text.strip()}")

        await asyncio.gather(reader(), writer())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBye")
