FROM maven:3.9-eclipse-temurin-17-alpine
WORKDIR /app
RUN apk add --no-cache python3 && mvn -version > /app/info.txt
COPY app.py .
EXPOSE 10000
CMD ["python3", "app.py"]
