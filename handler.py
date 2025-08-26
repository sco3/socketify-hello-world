from http.server import BaseHTTPRequestHandler

CONTENT_TYPE = "Content-Type"
TEXT_PLAIN = "text/plain"
HELLO = "Hello, World!\n"
UTF8 = "utf-8"
OK = 200
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(OK)
        self.send_header(CONTENT_TYPE, TEXT_PLAIN)
        self.end_headers()
        self.wfile.write(HELLO.encode(UTF8))
