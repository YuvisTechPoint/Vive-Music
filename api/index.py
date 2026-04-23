import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "music_club"))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_club.settings')

# Disable Django's debug toolbar in production
os.environ.setdefault('DISABLE_DEBUG_TOOLBAR', 'True')

try:
    import django
    from django.core.wsgi import get_wsgi_application
    from django.core.handlers.wsgi import WSGIHandler
    
    # Configure Django
    django.setup()
    
    # Create WSGI application
    application = get_wsgi_application()
    
    # For Vercel, we need to wrap the WSGI application
    def handler(event, context):
        return application(event, context)
    
    # Export the handler for Vercel
    app = handler
    
except Exception as e:
    # Fallback error handler
    def handler(event, context):
        return {
            'statusCode': 500,
            'body': f'Django setup failed: {str(e)}'
        }
    
    app = handler
