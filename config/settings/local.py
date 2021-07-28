from .base import *
from .base import env


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
        'NAME': env('MYSQL_NAME', default='databasename'),
        'USER': env('MYSQL_USER', default='databaseuser'),
        'PASSWORD': env('MYSQL_PASSWORD', default='databasepassword'),
        'HOST': env('MYSQL_HOST', default='localhost'),
        'PORT': env('MYSQL_PORT', default=3306),
}