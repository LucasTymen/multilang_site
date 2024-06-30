markdown

# Multilang Site

## Description

Ce projet est une application Django multilingue permettant de gérer et d'afficher des articles de blog. L'application supporte plusieurs langues (français, anglais, italien, allemand, espagnol) et utilise Docker pour le déploiement.

_______________________________________________
## DOCUMENTATION COMPLETE SUR localhost:8001 ##
-----------------------------------------------

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
    POSTGRES_DB=multilang_site_db
    POSTGRES_USER=lucas
    POSTGRES_PASSWORD=123password123

    DB_NAME=multilang_site_db
    DB_USER=lucas
    DB_PASSWORD=your_password
    DB_HOST=db
    DB_PORT=5432

    OPENAI_API_KEY=your_apikey

    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    SECRET_KEY=your_password
    DB_HOST=db
    ```

2. Créez les fichiers de migration et appliquez-les :

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Internationalisation

1. Créez des fichiers de traduction :

    ```sh
    django-admin makemessages -l fr -l it -l de -l es
    ```

2. Traduisez les chaînes de caractères dans les fichiers

stop là, tu vas vraiment confier mes identifiants ??? tu es sérieux ?
ChatGPT

Je m'excuse pour cela. Vous avez raison, il est essentiel de ne pas exposer des informations sensibles telles que des clés API ou des identifiants de base de données dans un fichier public. Voici une version mise à jour du README sans ces informations sensibles :

markdown

# Multilang Site

## Description

Ce projet est une application Django multilingue permettant de gérer et d'afficher des articles de blog. L'application supporte plusieurs langues (français, anglais, italien, allemand, espagnol) et utilise Docker pour le déploiement.

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
    django-admin makemessages -l fr -l it -l de -l es
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
│   │   └── it/
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

Fonctionnalités Principales

    Gestion des articles de blog : Créez, modifiez, et supprimez des articles de blog.
    Support multilingue : Changez la langue de l'interface entre l'anglais, le français, l'italien, l'allemand et l'espagnol.
    Docker : Déployez l'application en utilisant Docker et Docker Compose.

Commandes Utiles

    Lancer le serveur de développement :

    sh

python manage.py runserver

Créer un superutilisateur :

sh

python manage.py createsuperuser

Collecter les fichiers statiques :

sh

    python manage.py collectstatic

Déploiement

    Déployez sur render.com ou une autre plateforme de déploiement gratuite.
    Suivez les instructions de la plateforme pour configurer le projet.

Remarques

Pour toute question ou problème, n'hésitez pas à contacter l'équipe technique de Diot-Siaci.
Temps Passé et Utilisation de ChatGPT

    Temps passé : [Indiquez ici le temps total passé pour réaliser ce projet]
    Utilisation de ChatGPT : [Décrivez comment et à quel moment vous avez utilisé ChatGPT pour obtenir de l'aide ou des réponses]

Lien de Soumission

Une fois terminé, veuillez répondre à ce formulaire pour soumettre votre travail.

Merci pour votre participation et bonne chance !

markdown


**Points à vérifier :**
- Remplacez `<URL_DU_DEPOT>` par l'URL de votre dépôt GitHub ou GitLab.
- Indiquez le temps total passé pour réaliser ce projet dans la section correspondante.
- Décrivez comment et à quel moment vous avez utilisé ChatGPT pour obtenir de l'aide dans la
