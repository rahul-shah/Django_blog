import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret_setting('DATABASE_NAME'),
        'USER': get_secret_setting('DATABASE_USER'),
        'PASSWORD': get_secret_setting('DATABASE_PASSWORD'),
        'HOST': get_secret_setting('DATABASE_HOST'),
        'PORT': get_secret_setting('DATABASE_PORT'),
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'

STATIC_ROOT = 'static'