#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Add the project root to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Import and setup Django
import django
django.setup()

# Get the WSGI application
from django.core.wsgi import get_wsgi_application

# Create the application
application = get_wsgi_application()

# For Vercel serverless functions
def handler(event, context):
    return application(event, context)

# Export for Vercel
app = handler
