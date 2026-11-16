FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir python-jenkins
COPY app.py .
EXPOSE 10000
CMD ["python3", "app.py"]
