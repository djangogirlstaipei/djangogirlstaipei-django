from .base import *     # noqa

SECRET_KEY = ')#uqg@^y!&ei$l&l(*2ai3@+o8i+ju7vqryr6b+qtqq)na*#@='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = 'static'
