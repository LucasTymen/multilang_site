# openai_server/Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8003

CMD ["gunicorn", "openai_server.wsgi:application", "--bind", "0.0.0.0:8003", "--workers", "2"]
