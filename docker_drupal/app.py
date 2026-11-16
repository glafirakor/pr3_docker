import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = "<h1>Проект docker_drupal (CMS Drupal) успешно развернут на Render!</h1><p>Среда PHP 8.2 и ядро CMS Drupal подготовлены для управления контентом в облаке.</p>"
        self.wfile.write(html.encode('utf-8'))

port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
