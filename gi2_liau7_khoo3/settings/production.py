from .base import *

DEBUG = False

# Application definition
INSTALLED_APPS = SHARED_INSTALLED_APPS

STATIC_ROOT = os.path.join(BASE_DIR, 'staticAll')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
