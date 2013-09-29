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

def gen_func():
    return None

MOMMY_CUSTOM_FIELDS_GEN = {
    'autoslug.fields.AutoSlugField': gen_func,
}
