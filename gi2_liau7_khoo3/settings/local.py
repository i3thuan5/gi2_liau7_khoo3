from .base import *

# SECRET_KEY = get_env_variable('SOME_SECRET_KEY')

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}