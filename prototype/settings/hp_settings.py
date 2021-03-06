__author__ = 'Alexander'
from .settings import *
import sys

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'NAME': 'prototype',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': ''
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] [%(levelname)s %(levelno)s] [%(filename)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'consumer': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
