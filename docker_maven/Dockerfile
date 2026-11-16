FROM maven:3.9-eclipse-temurin-17
WORKDIR /app
RUN mvn -version > /app/info.txt
EXPOSE 10000
CMD ["sh", "-c", "echo 'HTTP/1.1 200 OK\nContent-Type: text/plain; charset=utf-8\n\nПроект docker_maven успешно развернут на Render!\n' | cat - /app/info.txt > /app/resp.txt && while true; do nc -l -p 10000 -q 1 < /app/resp.txt 2>/dev/null || python3 -m http.server 10000 -d /app; done"]
