# Use the official Python image from the Docker Hub
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

RUN groupadd --system app && useradd --system --gid app --create-home --home-dir /home/app app

COPY requirements.txt /code/
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . /code/
RUN chown -R app:app /code

USER app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn multilang_site.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 4"]
