# Usage

## Commandes Utiles

- **Lancer le serveur de développement** :

    ```sh
    python manage.py runserver
    ```

- **Créer un superutilisateur** :

    ```sh
    python manage.py createsuperuser
    ```

- **Collecter les fichiers statiques** :

    ```sh
    python manage.py collectstatic
    ```

## Utilisation de Docker

1. Construisez et démarrez les conteneurs Docker :

    ```sh
    docker-compose up --build
    ```

2. Accédez à l'application dans votre navigateur à `http://localhost:8000`.
