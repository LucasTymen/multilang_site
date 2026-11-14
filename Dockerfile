# Use Python 3.11+ for the patched Pillow version.
FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
