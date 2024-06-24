import os
import sys  # Import sys to use command-line arguments
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
SECRET_KEY = config('SECRET_KEY')  # Secret key for the Django application
DEBUG = config('DEBUG', default=False, cast=bool)  # Debug mode (should be False in production)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')  # Hosts/domain names that are valid for this site

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
    'compressor',  # For compressing and combining JavaScript and CSS files
    'modeltranslation',  # For translating Django models
    'rosetta',  # For managing translations through a web interface
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files in production
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
        'DIRS': [
            BASE_DIR / 'main/templates',
            BASE_DIR / 'templates',  # Adding the main templates directory
        ],  # Directories to search for templates
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
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',  # PostgreSQL database backend
            'NAME': config('DB_NAME'),  # Database name
            'USER': config('DB_USER'),  # Database user
            'PASSWORD': config('DB_PASSWORD'),  # Database password
            'HOST': config('DB_HOST'),  # Database host
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

# List of available languages
from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
    ('de', _('German')),
    ('zh-hans', _('Simplified Chinese')),
    ('ar', _('Arabic')),
    ('ru', _('Russian')),
    # Add more languages here
]

LOCALE_PATHS = [BASE_DIR / 'locale']

# Static files
STATIC_URL = '/static/'  # URL for serving static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directories to search for static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory to collect static files

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
