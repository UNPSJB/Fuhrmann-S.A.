"""
Django settings for pFuhrmann project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from local_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGIN_URL = 'mysite_login'
LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/'# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o#go!yw@0f-e9i7!^uy86yt%8#=an!oi$utb^ggok09odg*5ua'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',

    'django_extensions',
    'appWeb',
    'crispy_forms',
  #  'wkhtmltopdf',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

)

ROOT_URLCONF = 'pFuhrmann.urls'

WKHTMLTOPDF_CMD = '/path/to/my/wkhtmltopdf'
WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': True,
}


WSGI_APPLICATION = 'pFuhrmann.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

SITE_ID = 1

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
     'templates',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#STATIC_ROOT = '/home/matth/mysiteagencia/static/'
STATIC_URL = '/static/'
#'http://localhost:80/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows. 
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(BASE_DIR, 'static'),
    'static',
)

CRISPY_TEMPLATE_PACK= 'bootstrap3'
