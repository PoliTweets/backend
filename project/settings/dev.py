# -*- coding: utf-8 -*-

from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BROKER_POOL_LIMIT = 1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# import dj_database_url
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
