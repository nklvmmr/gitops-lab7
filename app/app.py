from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def get_data():
    return {"app": "telemetry", "version": "v2", "temperature": 22}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"ok"
        else:
            body = json.dumps(get_data()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8116), Handler).serve_forever()
