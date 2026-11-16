FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir python-jenkins
EXPOSE 10000
CMD ["python3", "-c", "from http.server import BaseHTTPRequestHandler, HTTPServer; import os, jenkins; \
class H(BaseHTTPRequestHandler): \
  def do_GET(self): \
    self.send_response(200); self.send_header('Content-type','text/html; charset=utf-8'); self.end_headers(); \
    self.wfile.write(f'<h1>Проект docker_jenkins успешно развернут на Render!</h1><p>Библиотека Jenkins CI/CD (версия: {jenkins.__version__}) установлена и работает в облаке.</p>'.encode('utf-8')); \
HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 10000))), H).serve_forever()"]
