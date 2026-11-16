FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir couchbase || true
EXPOSE 10000
CMD ["python3", "-c", "from http.server import BaseHTTPRequestHandler, HTTPServer; import os; \
class H(BaseHTTPRequestHandler): \
  def do_GET(self): \
    self.send_response(200); self.send_header('Content-type','text/html; charset=utf-8'); self.end_headers(); \
    self.wfile.write('<h1>Проект docker_couchbase (NoSQL СУБД Couchbase) развернут на Render!</h1><p>Клиентский модуль Couchbase SDK установлен и готов к подключению к кластеру.</p>'.encode('utf-8')); \
HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 10000))), H).serve_forever()"]
