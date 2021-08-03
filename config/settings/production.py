
from .base import *
import dj_database_url
import django_heroku


django_heroku.settings(locals())


DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
