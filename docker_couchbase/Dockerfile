FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir couchbase || true
COPY app.py .
EXPOSE 10000
CMD ["python3", "app.py"]
