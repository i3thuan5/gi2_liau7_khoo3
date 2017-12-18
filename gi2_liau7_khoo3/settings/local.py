from .base import *

DEBUG = True

# Local SECRET_KEY 
SECRET_KEY = 'LocalsecretkeyforGi2liau7khoo3'
        
# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
] + SHARED_INSTALLED_APPS
