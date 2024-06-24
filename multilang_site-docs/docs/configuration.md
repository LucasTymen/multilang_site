# Configuration

## Fichier .env

Créez un fichier `.env` dans le répertoire principal avec le contenu suivant :

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


Paramètres Django

Assurez-vous que settings.py est correctement configuré pour utiliser les variables d'environnement définies dans le fichier .env.


from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
