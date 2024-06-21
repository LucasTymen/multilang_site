import os
from pathlib import Path
from decouple import config  # Use decouple for better environment variable management
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Security
SECRET_KEY = config('SECRET_KEY', default='aze"é&AZE321')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin site
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static file handling
    'main',  # Your main application
    'django.contrib.sites',  # Sites framework (required for django-allauth)
    'allauth',  # Allauth application for authentication
    'allauth.account',  # Account management for allauth
    'allauth.socialaccount',  # Social account management for allauth
    'crispy_forms',  # Crispy forms for better form rendering
    'crispy_bootstrap5',  # Crispy forms template pack for Bootstrap 5
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.locale.LocaleMiddleware',  # Locale middleware for internationalization
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
    'allauth.account.middleware.AccountMiddleware',  # Account middleware for allauth
]

# URL configuration
ROOT_URLCONF = 'multilang_site.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django template backend
        'DIRS': [BASE_DIR / 'templates'],  # Directories to search for templates
        'APP_DIRS': True,  # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Auth context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'multilang_site.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # PostgreSQL database backend
        'NAME': config('DB_NAME', default='multilang_site_db'),  # Database name
        'USER': config('DB_USER', default='lucas'),  # Database user
        'PASSWORD': config('DB_PASSWORD', default='123password123'),  # Database password
        'HOST': config('DB_HOST', default='db'),  # Database host
        'PORT': config('DB_PORT', default='5432'),  # Database port
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # User attribute similarity validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validator
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'  # Default language code
TIME_ZONE = 'UTC'  # Default time zone
USE_I18N = True  # Use internationalization
USE_L10N = True  # Use localization
USE_TZ = True  # Use time zones

# Static files
STATIC_URL = '/static/'  # URL for serving static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directories to search for static files

# Media files
MEDIA_URL = '/media/'  # URL for serving media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory to store media files

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Authentication backend for allauth
)

SITE_ID = 1  # Required for django-allauth

# URL configuration for allauth
LOGIN_REDIRECT_URL = '/'  # Redirect URL after login
LOGOUT_REDIRECT_URL = '/'  # Redirect URL after logout

# Crispy forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
