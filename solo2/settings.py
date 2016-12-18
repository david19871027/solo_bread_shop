"""
Django settings for solo2 project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=#eeo8vgo6&s+v&zs0=^##1-6t-3$%i(f9-82h$#-8zt@wb(y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'rest_framework',
    'rest_framework_swagger',
	'seller'
]


# REST_FRAMEWORK

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
	'PAGE_SIZE': 10,
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	)
}


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'solo2.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'solo2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.contrib.gis.db.backends.postgis",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "solo2",
        "USER": "postgres",
        "PASSWORD": "pbn6h9E",
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, *MEDIA_URL.strip("/").split("/"))

# For dev
STRIPE_KEYS = {
    'API_KEY': 'sk_test_1AFSPD5Dg8RihyPPtylWiSsR',
    'PUBLIC_KEY': 'pk_test_Q4RGBzPFhWbMP2daCqMg6Rj7',
    # 'CLIENT_ID': 'ca_8Qcy5FPjST3HuFl7xXjisiodyjKE5d8V',
}

# twilio credentials
TWILIO_ACCOUNT_SID = "ACb311a23eddf63e73d3812c07921b540c" 
TWILIO_AUTH_TOKEN = "6bf4a906976eb9f31d683dd336be4784" 

TOKEN_SECRET = '098098ug034hg34g934f343o#G#G$#$#$G'

AUTH_USER_MODEL = 'seller.Baker'

FACEBOOK_SECRET = '3c9a68e9d6a29b6f240112c7c6998b70'
TWITTER_CONSUMER_KEY = 'J6eeF1zgj7CmGGBO5ARPMPbrC'
TWITTER_CONSUMER_SECRET = 'OMcmHxnOBIR6VdIBshsznk25P6VpWTHfVyQBZ63JMaluGOLbsW'
TWITTER_CALLBACK_URL = 'http://127.0.0.1:8000/auth/twitter'

EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_HOST_USER = 'AKIAJQWFUMH5MCIHX52Q' #'ses-smtp-user.20160616-182855'
EMAIL_HOST_PASSWORD = 'AlETX02PSbQI8a46g7RL/cN7lbzF9sBHbOTag+TUOxxv'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@getfreshbaked.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'