"""
ASGI config for music_club project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Ensure Django is setup before trying to get the application
django.setup()

# Try ASGI first, fallback to WSGI for Vercel
try:
    application = get_asgi_application()
except:
    application = get_wsgi_application()
