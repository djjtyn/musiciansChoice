"""
Django settings for musicians_choice project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url
# Import the file that has the environment variables
if os.path.exists("env.py"):
    import env as env_variables
    
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'udyc$t%ziearxfpo)dpi2d56yaj&cj&8j&552ip_huah3(g*32'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '135a869bdf7049fa82691162b8a41ef4.vfs.cloud9.eu-west-1.amazonaws.com', 
    'django-env.eba-f3mtanzm.eu-west-1.elasticbeanstalk.com',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'home',
    'users',
    'brands',
    'comments',
    'instrument_type',
    'instruments',
    'orders',
    'storages',
    'cart',
    'payment',
    'sns_notifications',
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

ROOT_URLCONF = 'musicians_choice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents',
            ],
        },
    },
]

WSGI_APPLICATION = 'musicians_choice.wsgi.application'


# Database
# If there is a environment variable for the database use that databases details
# if env_variables:
#     print("Found hosted DB connection to use")
# try:
#     if os.path.exists("env.py"):
#         DATABASES = {
#             'default':  dj_database_url.parse(env_variables.get_db_url())
#         }
#     else :
#         DATABASES = {
#             'default':  dj_database_url.parse(os.environ.get('db_url'))
#         }
#     # If there is an issue using the hosted database revert to sqlite 3
# except:
#     print("Issue identified while trying to use hosted db. Switching to SQLite3")
#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
# else:
print("No hosted database details found. Using SQLite")
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Set the custom user model as the authentication model
AUTH_USER_MODEL = "users.CustomUser"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Connection to the static folder
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if os.path.exists("env.py"):
    #Stripe Details
    STRIPE_PUBLISHABLE_KEY = env_variables.get_stripe_publishable()
    STRIPE_SECRET_KEY = env_variables.get_stripe_secret()
    #AWS S3 Details
    AWS_ACCESS_KEY_ID = env_variables.get_aws_access_key()
    AWS_SECRET_ACCESS_KEY = env_variables.get_aws_secret_key()

else:
    #Stripe Details
    STRIPE_PUBLISHABLE_KEY = os.environ.get('stripe_publishable')
    STRIPE_SECRET_KEY = os.environ.get('stripe_secret')
    #AWS S3 Details
    AWS_ACCESS_KEY_ID = os.environ.get('aws_access_key')
    AWS_SECRET_ACCESS_KEY = os.environ.get('aws_secret_key')
  
AWS_STORAGE_BUCKET_NAME = 'musicianschoicepics'
AWS_S3_REGION_NAME = 'eu-west-1' 
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
INSTRUMENT_IMAGE_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/" 

    
