"""
Django settings for damat_project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jfkvf2s**(gyc3-*g4as8m_z7a5no$071yldii+i=yy3_$x7c+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get('DEBUG') else True
PROD =  not DEBUG
ALLOWED_HOSTS = ['*']

if PROD:
    DEV_HOST='http://localhost/'
else:
    DEV_HOST='http://localhost:8000/'


# Application definition

APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
APPS.insert(0, 'jet.dashboard', )

APPS.insert(0, 'jet')

CUSTOME_APPS = [
    'account',
    'blog',
    'contact.apps.ContactConfig',
    'product.apps.ProductConfig',
    'index',
    'menu',
    'order',
    # 'mptt',
    # 'modeltrans',
    'debug_toolbar',
]

THIRD_PARTY_APPS = [

    'social_django',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    # CORS
    'corsheaders',
]

INSTALLED_APPS = APPS + CUSTOME_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'damat_project.middleware.force_default_middleware.force_default_language_middleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# CORS
CORS_ALLOW_ALL_ORIGINS = True

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'az'

# ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'az'
USE_I18N = True
USE_L10N = True

ROOT_URLCONF = 'damat_project.urls'

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
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'damat_project.wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {

#     }
# }

if PROD:
    print(PROD, 'Porduction Mode')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PORT': os.environ.get('POSTGRES_PORT'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
        }
    }
else:
    print('Development Mode')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'damats_db',
            'USER': 'admin_damat',
            'PORT': 5435,
            'PASSWORD': 'elvin123',
            'HOST': '127.0.0.1',
        }
    }

if PROD:
    CELERY_BROKER_URL = 'redis://redis:6379'
    CELERY_RESULT_BACKEND = 'redis://redis:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Baku'
else:
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Baku'

# SCOIAL AUTH CONFIGRATION

AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = '219950869707977'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '1f1682843bb8cedfae6beb09cd64b8b2'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '871788835099-4buoe7ru6d3s0bt4qmshll7qi9fdkb43.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6K0zpu08FvWqJsBVNL5B6BrD'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']  # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email,picture',
}

SOCIAL_AUTH_URL_NAMESPACE = 'social'  # namespace

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',

    'account.tools.social_auth.update_user_social_data',  # custom pipeline
)

# REST API AUTHENTICATION USER FOR API
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.AllowAny', ),
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'tr'

gettext = lambda s: s
LANGUAGES = [
    ('tr', gettext('Turkish')),
    ('az', gettext('Azerbaijan')),
    ('ar', gettext('Arabic')),
    ('ru', gettext('Russian')),
    ('it', gettext('Italian')),
    ('en', gettext('English')),
]

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
else:
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SITE_ADDRESS = 'http://localhost:8000'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'
MODELTRANSLATION_LANGUAGES = ('tr', 'en', 'az', 'ar', 'ru', 'it',)
MODELTRANSLATION_FALLBACK_LANGUAGES = ('tr', 'en', 'tr', 'ar', 'ru', 'it',)
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'tr'
MODELTRANSLATION_TRANSLATION_FILES = (
    "product.translation",
)


JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
LOGIN_URL = reverse_lazy('account:login')

LOGIN_REDIRECT_URL = reverse_lazy('index:home')  # login olandan sora redirect olacaq sehife
LOGOUT_REDIRECT_URL = reverse_lazy('index:home')  # logout olandan sora redirect olacaq sehife

LOGOUT_URL = reverse_lazy('account:logout')




# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'husubayli@gmail.com'
EMAIL_HOST_PASSWORD = 'xdjnasiuddxikfax'

# SITE_ADDRESS = 'http://localhost:8000'


