import os
from common import *

DEBUG = TEMPLATE_DEBUG = True
INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS += (
    'django_extensions',
)

STATIC_URL = '/static/'

DATABASES = {'default' : {'ENGINE' : 'django.db.backends.sqlite3', 'NAME' : os.path.join(os.path.dirname(__file__),'../data.db')}}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
