import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Import and configure Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
