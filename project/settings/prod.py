# -*- coding: utf-8 -*-

from defaults import *

DEBUG = False

ALLOWED_HOSTS = [
    'politweets-prod.herokuapp.com',
    'politweets.rts.ch'
]

SITE_ID = 3  # Local=1, Staging=2, Prod=3

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'politweets',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'politweets',
        'PASSWORD': 'CnOZZVQGR4HT',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}
