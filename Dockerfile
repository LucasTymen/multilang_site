# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Installer les dépendances système et nettoyer le cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    build-essential \
    libpq-dev \
    python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt et les installer
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . /app

# Exposer le port de l'application
EXPOSE 8000

# Définir la commande de démarrage par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
