from .base import *

DEBUG = False

# Production SECRET_KEY 
# WARNING: keep the secret key used in production secret!
try:
    with open(BASE_DIR + '/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error for SECRET_KEY.")
    raise

# Application definition
INSTALLED_APPS = SHARED_INSTALLED_APPS

STATIC_ROOT = os.path.join(BASE_DIR, 'whitenoise_static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
