""" Settings required by django-progressive-web-app. """
from django.conf import settings
import os

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates', 'serviceworker.js'))

# App parameters to include in manifest.json and appropriate meta tags
# Build manifest.json
PWA_APP_NAME = 'Venclefit' 
PWA_APP_DESCRIPTION = "내가 원하는 나를 향한 여정: Venclefit" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#ffffff' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any' 
PWA_APP_START_URL = '/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ 
    { 
        'src': '/static/images/icon-160x160.png', 
        'sizes': '160x160' 
    } 
] 
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/images/icon-160x160.png',
        'sizes': '160x160'
    }
]
