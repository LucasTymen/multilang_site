# Multilang Site

## Description

Ce projet est une application Django multilingue permettant de gérer et d'afficher des articles de blog. L'application supporte plusieurs langues (français, anglais, italien, allemand, espagnol, japonais) et utilise Docker pour le déploiement.

## Prérequis

- Python 3.9+
- Docker
- Docker Compose

## Installation

1. Clonez le dépôt :

    ```sh
    git clone <URL_DU_DEPOT>
    cd multilang_site
    ```

2. Créez et activez un environnement virtuel :

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Installez les dépendances :

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Créez un fichier `.env` dans le répertoire principal avec le contenu suivant :

    ```ini
    POSTGRES_DB=your_postgres_db
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password

    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=db
    DB_PORT=5432

    OPENAI_API_KEY=your_openai_api_key

    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    SECRET_KEY=your_secret_key
    ```

2. Créez les fichiers de migration et appliquez-les :

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Internationalisation

1. Créez des fichiers de traduction :

    ```sh
    django-admin makemessages -l fr -l it -l de -l es -l ja
    ```

2. Traduisez les chaînes de caractères dans les fichiers `.po`.

3. Compilez les fichiers de traduction :

    ```sh
    django-admin compilemessages
    ```

## Utilisation de Docker

1. Construisez et démarrez les conteneurs Docker :

    ```sh
    docker-compose up --build
    ```

2. Accédez à l'application dans votre navigateur à `http://localhost:8000`.

## Structure du Projet

```plaintext
multilang_site/
├── db.json
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── env/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── locale/
│   │   ├── de/
│   │   ├── es/
│   │   ├── fr/
│   │   ├── it/
│   │   ├── ja/
│   │   └── en/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_article_categories_and_more.py
│   │   ├── __init__.py
│   │   └── __pycache__/
│   ├── models.py
│   ├── __pycache__/
│   ├── signals.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── main/
│   │       ├── article_detail.html
│   │       ├── article_form.html
│   │       ├── article_list.html
│   │       ├── base.html
│   │       ├── delete_account.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media/
│   └── profile_pics/
├── multilang_site/
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Pipfile
├── Pipfile.lock
├── readme.txt
└── requirements.txt
