import os
import jenkins
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = f"<h1>Проект docker_jenkins успешно развернут на Render!</h1><p>Библиотека Jenkins CI/CD (версия: {jenkins.__version__}) установлена и работает в облаке.</p>"
        self.wfile.write(html.encode('utf-8'))

port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
