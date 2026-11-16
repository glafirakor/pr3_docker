FROM maven:3.9-eclipse-temurin-17-alpine
WORKDIR /app
RUN apk add --no-cache python3 && mvn -version > /app/info.txt
EXPOSE 10000
CMD ["python3", "-c", "from http.server import BaseHTTPRequestHandler, HTTPServer; import os; \
info = open('/app/info.txt').read(); \
class H(BaseHTTPRequestHandler): \
  def do_GET(self): \
    self.send_response(200); self.send_header('Content-type','text/html; charset=utf-8'); self.end_headers(); \
    self.wfile.write(f'<h1>Проект docker_maven успешно развернут на Render!</h1><pre>{info}</pre>'.encode('utf-8')); \
HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 10000))), H).serve_forever()"]
