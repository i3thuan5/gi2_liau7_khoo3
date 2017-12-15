from .base import *

DEBUG = True

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
] + SHARED_INSTALLED_APPS
