from .base import *

DEBUG = False

# Application definition
INSTALLED_APPS = SHARED_INSTALLED_APPS

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
