from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_5=#=+cl&lp@&ayps6ia0viff)^v$_wvutyyxca!xu0w6d2z3$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

RECAPTCHA_USE_SSL = False
SECURE_SSL_REDIRECT = False
NOCAPTCHA = False
