import os
import sys
from pathlib import Path

# Set up the path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Import Django
import django
from django.core.wsgi import get_wsgi_application

django.setup()

application = get_wsgi_application()

# Export a real WSGI app for Vercel.
app = application
handler = application
