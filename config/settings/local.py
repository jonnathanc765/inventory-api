from .base import *
from .base import env


# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH')

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-extensions
INSTALLED_APPS += ['django_extensions'] 

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025


DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': env('MYSQL_HOST', default='localhost'),
    'PORT': env('MYSQL_PORT', default=3306),
    'NAME': env('MYSQL_DATABASE', default='databasename'),
    'USER': env('MYSQL_USER', default='databaseuser'),
    'PASSWORD': env('MYSQL_PASSWORD', default='databasepassword'),
}
