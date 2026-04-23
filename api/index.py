import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "music_club"))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

import django
from django.core.wsgi import get_wsgi_application

django.setup()

application = get_wsgi_application()

# Export a real WSGI app for Vercel.
app = application
handler = application
