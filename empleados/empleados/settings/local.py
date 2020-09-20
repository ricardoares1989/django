"""
Django settings local for empleados project.
"""
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbempleados',
        'USER': 'WtSsWWkkvUMOZKEergaBWpMQqYUsmtFm',
        'PASSWORD': 'nUOBbYbiaoj0ZTgp5CNZ4JvAbTCw0lvfAUqElrr4tCBOKVQPpC0QWGZ1qiOfCd9j',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.with_name('static')]

