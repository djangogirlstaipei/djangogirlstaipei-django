import os
from django.conf import ENVIRONMENT_VARIABLE
from django.core.exceptions import ImproperlyConfigured


if os.environ.get(ENVIRONMENT_VARIABLE) == '__.settings':
    raise ImproperlyConfigured(
        'Do not use this file. Use --settings= to specify a settings module. '
        'If you don\'t know what to use, try "--settings=__.settings.dev".'
    )
