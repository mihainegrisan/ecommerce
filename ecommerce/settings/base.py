import os
from django.contrib.messages import constants as messages
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = os.environ.get('SECRET_KEY_MIHAI_SHOP')
SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # own apps
    'core.apps.CoreConfig',
    'shop.apps.ShopConfig',

    # third-party apps
    'crispy_forms',
    # 'taggit',
    'django.contrib.sites',
    # 'django.contrib.sitemaps',
    'storages',
    'admin_honeypot',
    # 'widget_tweaks',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'rest_auth',
    'django_countries',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'ecommerce:home'
LOGOUT_REDIRECT_URL = 'ecommerce:home'
LOGIN_URL = '/accounts/login/'

# I'm changing just the tag of the error so that bootstrap4 alert and messages tags to be the same (danger).
# so messages.error -> tags == danger
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# EMAIL CONFIGURATION
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# django-storages & AWS settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID_MIHAI_BUSINESS')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_MIHAI_BUSINESS')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME_MIHAI_BUSINESS')
# If a user uploads a file with the same name as another user's filename .. don't overwrite the file... just add it with a different name
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'eu-central-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# To allow django-admin.py collectstatic to automatically put your static files in your bucket set the following in your settings.py:
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# MAILCHIMP
MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER = os.environ.get('MAILCHIMP_DATA_CENTER')
MAILCHIMP_EMAIL_LIST_ID = os.environ.get('MAILCHIMP_EMAIL_LIST_ID')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# STRIPE DEVELOPMENT KEY
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')


django_heroku.settings(locals())
