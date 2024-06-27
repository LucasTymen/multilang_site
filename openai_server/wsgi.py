# openai_server/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.append('/openai_server')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openai_server.settings')

application = get_wsgi_application()
