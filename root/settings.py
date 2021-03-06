"""
Django settings for root root.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the root like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

AUTH_USER_MODEL = 'accounts.User'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #my apps
    'accounts',
    'picture',
    'album',

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party apps
    'rest_framework',
    'djoser',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'drf_yasg',
    'storages'



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'root.wsgi.application'


# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOWED_ORIGINS = ()
#CORS_ALLOW_CREDENTIALS = True # ?????????????????? ?????????????????????????? ?????????? ?????? ??????????-???????????????? ????????????????

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'EXCEPTION_HANDLER': 'picture.utils.custom_exception_handler'
}
# SIMPLE_JWT SETTINGS
if DEBUG:
    access_token_lifetime = timedelta(days=5)
else:
    access_token_lifetime = timedelta(minutes=15)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': access_token_lifetime,
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
}

# DJOSER SETTINGS
#DEFAULT_USER_SERIALIZER = 'users.serializers.CustomUserSerializer'
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SET_PASSWORD_RETYPE': True,
    'SERIALIZERS': {
        # 'user_create': DEFAULT_USER_SERIALIZER,  # checked
        # 'user': DEFAULT_USER_SERIALIZER,  # checked
        'current_user': 'accounts.serializers.UserSerializer',  # checked
        # 'activation': 'djoser.serializers.ActivationSerializer',  # checked
        # 'password_reset': 'djoser.serializers.SendEmailResetSerializer', # checked
        # 'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer', # checked
        # 'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        # 'set_password': 'djoser.serializers.SetPasswordSerializer', # checked
        # 'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        # 'set_username': 'djoser.serializers.SetUsernameSerializer',# checked
        # 'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
        # 'username_reset': 'djoser.serializers.SendEmailResetSerializer',# checked
        # 'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',# checked
        # 'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',# checked
        # 'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',# checked
        # 'user_delete': 'djoser.serializers.UserDeleteSerializer',# checked

    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
import pymysql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DATABASE_NAME"),
        'HOST': os.getenv("DATABASE_HOST"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'PORT': os.getenv("DATABASE_PORT"),
        'ATOMIC_REQUESTS': True  # ???????????? ???? ??????????????????????
    }
}
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            'OPTIONS': {
                'min_length': 7
            }
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# if DEBUG:
#     MEDIA_URL = '/media/'
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static')
#     ]
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


API_VERSION = 'v1'
API_URL = 'api/%s/' % API_VERSION


# AWS SETTINGS

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")

# S3
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", "cloud-shutterstock-bucket")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


# CELERY
CELERY_BROKER_URL = 'redis://localhost:6379'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  
CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TASK_SERIALIZER = 'json'  


# REDIS
REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'