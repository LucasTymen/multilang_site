# Utiliser l'image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /code

# Copier les fichiers de requirements
COPY requirements.txt /code/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . /code/

# Exposer le port utilisé par Django
EXPOSE 8000

# Définir la commande par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
