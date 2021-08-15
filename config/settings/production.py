
# import os
from .base import *
import dj_database_url
import django_heroku


django_heroku.settings(locals())

print(INSTALLED_APPS)


DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
