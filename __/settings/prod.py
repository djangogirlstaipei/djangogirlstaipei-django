from .base import *     # noqa
import dj_database_url

SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['djangogirlstaipei.herokuapp.com']

STATIC_ROOT = 'static'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
