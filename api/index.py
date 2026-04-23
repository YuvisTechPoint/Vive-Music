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
from django.http import HttpResponse

# Create the WSGI application
application = get_wsgi_application()

# Custom middleware to handle common Vercel issues
class VercelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Handle OPTIONS requests for CORS
        if request.method == 'OPTIONS':
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-CSRFToken'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response

        # Get the original response
        response = self.get_response(request)

        # Add CORS headers
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-CSRFToken'
        response['Access-Control-Allow-Credentials'] = 'true'

        # Fix for Vercel deployment issues
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['X-Content-Type-Options'] = 'nosniff'

        return response

# Apply the middleware
def application_with_middleware(environ, start_response):
    from django.core.handlers.wsgi import WSGIHandler
    django_app = WSGIHandler()
    
    def custom_start_response(status, headers, exc_info=None):
        # Add custom headers
        headers.append(('Access-Control-Allow-Origin', '*'))
        headers.append(('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'))
        headers.append(('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-CSRFToken'))
        headers.append(('Access-Control-Allow-Credentials', 'true'))
        return start_response(status, headers, exc_info)
    
    return django_app(environ, custom_start_response)

# Use the custom application
application = application_with_middleware
