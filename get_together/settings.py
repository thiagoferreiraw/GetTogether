"""
Django settings for get_together project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e%_(opi$sv5aaeo=64lq8j4v5ia6sbtg9)hmp1^h8b&-7=#=67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID=1
ADMINS = [ 'mhall119' ]

# Application definition

INSTALLED_APPS = [
    'get_together',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'django.contrib.sites',
    'rest_framework',
    'social_django',
    'imagekit',
    'imagekit_cropper',
    'mptt',
    'recurrence',

    'events',
    'accounts',
    'resume',
    'simple_ga',
    'totd',
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
SETUP_URL = 'profile/+confirm_profile'
LOGIN_REDIRECT_URL = 'home'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
#    'social_core.backends.linkedin.LinkedinOAuth2',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
    'resume.middleware.ResumeMiddleware',
    'simple_ga.middleware.GAEventMiddleware',
]

ROOT_URLCONF = 'get_together.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django_settings_export.settings_export',
                'simple_ga.context_processors.events',
                'totd.context_processors.tips',
                'accounts.decorators.check_setup',
             ],
        },
    },
]

WSGI_APPLICATION = 'get_together.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

db_engine = os.environ.get("DB_ENGINE", "postgresql")

if db_engine == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DATABASE_NAME", "postgres"),
            "USER": os.environ.get("DATABASE_USER", "postgres"),
            "PASSWORD": os.environ.get("DATABASE_PASSWORD", "root"),
            "HOST": os.environ.get("DATABASE_HOST", "localhost"),
            "PORT": os.environ.get("DATABASE_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'TEST': {
                'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
            }
        }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = [
    './get_together/locale',
]

USE_TZ = True
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'
# MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'

MATOMO_HOST=None
MATOMO_SITE_ID=None

IPSTACK_ACCESS_KEY=None
GOOGLE_ANALYTICS_ID=None
GOOGLE_MAPS_API_KEY=None
SOCIAL_AUTH_GITHUB_KEY=None
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=None
SOCIAL_AUTH_FACEBOOK_KEY=None
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.12'
SOCIAL_AUTH_TWITTER_KEY=None
SOCIAL_AUTH_LINKEDIN_KEY=None
SOCIAL_AUTH_LINKEDIN_SECRET=None
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address']
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address')]
SETTINGS_EXPORT = [
    'DEBUG',
    'GOOGLE_ANALYTICS_ID',
    'GOOGLE_MAPS_API_KEY',
    'SOCIAL_AUTH_GITHUB_KEY',
    'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',
    'SOCIAL_AUTH_FACEBOOK_KEY',
    'SOCIAL_AUTH_TWITTER_KEY',
    'SOCIAL_AUTH_LINKEDIN_KEY',
    'IPSTACK_ACCESS_KEY',
    'MATOMO_SITE_ID',
    'MATOMO_HOST',
]

# Make django messages framework use Bootstrap's alert style classes
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Keep this at the end of settings.py to allow overriding settings in local deployments
try:
    from local_settings import *

except:
    print("WARNING: You should create a local_settings.py to store local and secret data.")



# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())