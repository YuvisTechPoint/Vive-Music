import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Set Vercel environment variable
os.environ.setdefault('VERCEL', 'true')

# Import and configure Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application

# Create the WSGI application
application = get_wsgi_application()

# Add CORS headers for Vercel
def cors_headers_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-CSRFToken'
        return response
    return middleware

# Apply CORS middleware
application = cors_headers_middleware(lambda _: application)
