FROM php:8.2-cli-alpine
WORKDIR /app
RUN apk add --no-cache python3
COPY app.py .
EXPOSE 10000
CMD ["python3", "app.py"]
