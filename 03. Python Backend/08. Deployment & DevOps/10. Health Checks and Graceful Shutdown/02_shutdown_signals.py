# 02 — Graceful shutdown signals
# Run: python 02_shutdown_signals.py

import signal
import time

_shutdown = False


def handle_signal(signum, frame):
    global _shutdown
    print(f"\nReceived signal {signum}, finishing in-flight work...")
    _shutdown = True


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    print("Simulating worker loop (Ctrl+C to graceful-stop)...")
    while not _shutdown:
        print("working...", flush=True)
        time.sleep(1)
    print("Cleanup done. Exit.")
