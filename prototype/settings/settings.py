"""
Django settings for prototype project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ua6ankbbg9rhp(bo_(jn-nw%%)7(fp06^+*eofjqrm2v=6e@vo'

try:
    owner = __file__.split('/')[2].lower()
except:
    owner = __file__.split('\\')[2].lower()

devs = ['mahome']
if owner in devs:
    WHICH = '{}_settings'.format(owner)
else:
    WHICH = 'prod_settings'

# Application definition

INSTALLED_APPS = [
    # 'grappelli',
    # 'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'django.contrib.humanize',
    'subdomains',
    'simple_sso.sso_server'
]

ROOT_URLCONF = 'prototype.urls.schools'
AUTH_USER_MODEL = 'core.User'

SITE_ID = 1

SUBDOMAIN_URLCONFS = {
    None: 'prototype.urls.root',  # no subdomain, e.g. ``example.com``
    'www': 'prototype.urls.root',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES_DIR = os.path.join(BASE_DIR, '../core/templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'prototype.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SSO SERVER SETTING
SSO_PRIVATE_KEY = 'ua6ankbbg9rhp(bo_(jn-nw%%)7(fp06^+*eofjqrm2v=6e@vo'
SSO_PUBLIC_KEY = '_yrucn5!dgeteec1*vt)1ca!oa$8)keiwd%pj!x34ved*c#8y5'
SSO_SERVER = 'http://schools.com/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '../static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../core/static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

AFTER_RESPONSE_RUN_ASYNC = True

# EMAIL PARAMETERS SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "Schoolify <info@schoolify.ng>"

EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.schoolify.ng'
EMAIL_HOST_USER = 'info@schoolify.ng'
EMAIL_HOST_PASSWORD = 'computergeek#1'
EMAIL_PORT = 2525

# PAYSTACK PARAMETER SETTINGS
PAYSTACK_KEY = ''

# GOOGLE PARAMETER SETTINGS
GOOGLE_MAP_KEY = 'AIzaSyBFrI6YNR_cxLJJFwHSk815_U9yHGr_H9c'

# FILE BROWSER SETTINGS
DATA_UPLOAD_MAX_MEMORY_SIZE = None
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520

UPLOADS_DIR = os.path.dirname(BASE_DIR)
FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''
