from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT_PATH.child('db.sqlite3'),
        'TEST_NAME': PROJECT_ROOT_PATH.child('db-test.sqlite3'),
    }
}

# Tests configuration
SOUTH_TESTS_MIGRATE = False
