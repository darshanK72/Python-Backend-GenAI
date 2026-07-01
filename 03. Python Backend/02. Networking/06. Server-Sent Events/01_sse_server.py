# 01 — SSE server (stdlib HTTP)
# Run: python 01_sse_server.py
# Then: python 02_sse_client.py

import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
PORT = 8787


class SSEHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/events":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        for i in range(5):
            payload = f"data: event {i} at {time.strftime('%H:%M:%S')}\n\n"
            self.wfile.write(payload.encode())
            self.wfile.flush()
            time.sleep(1)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), SSEHandler)
    print(f"SSE server http://{HOST}:{PORT}/events")
    server.serve_forever()
