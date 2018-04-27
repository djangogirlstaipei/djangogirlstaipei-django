import dj_database_url

from .base import get_env_var, DATABASES

SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['djangogirlstaipei.herokuapp.com']

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STATIC_ROOT = 'static'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
