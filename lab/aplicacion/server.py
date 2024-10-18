import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        message = f'''
        <!DOCTYPE html>
        <html>
            <body>
                <h1>Hello, World!</h1>
                <p>your IP address is `{self.client_address[0]}`</p>
            </body>
        </html>'''

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

# socketserver.TCPServer permite que el servidor escuche en todas las interfaces con '' o '0.0.0.0'
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
