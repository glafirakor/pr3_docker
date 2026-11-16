import os
from http.server import BaseHTTPRequestHandler, HTTPServer

info = open('/app/info.txt').read()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = f"<h1>Проект docker_maven успешно развернут на Render!</h1><pre>{info}</pre>"
        self.wfile.write(html.encode('utf-8'))

port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
