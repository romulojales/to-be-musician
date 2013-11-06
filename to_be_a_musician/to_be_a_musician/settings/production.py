import dj_database_url
from .base import *

DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static configuration
STATIC_ROOT = PROJECT_ROOT_PATH.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_ROOT_PATH.child('static'),
)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
