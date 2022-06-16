from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "drf_yasg",
    "django_celery_results",
    "django_celery_beat",
    "django_filters",

    "youtube_videos",
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

ROOT_URLCONF = 'circulo.urls'

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

WSGI_APPLICATION = 'circulo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('db_name'),
        'USER': env('db_user'),
        'PASSWORD': env('db_password'),
        'HOST': env('db_host'),
        'PORT': env('db_port'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_SAVE_EVERY_REQUEST = True

CELERY_BROKER_URL = env("REDIS_URL")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_RESULT_BACKEND = "django-db"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

QUERY = "football"
MIN_INTERVAL = 5
INTERVAL = 10
MAX_INTERVAL = 60*60
THRESHOLD = 15
MULTIPLICATION_FACTOR = 2

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'youtube_videos': '65/min',
    }
}

DEFAULT_FROM_EMAIL = "hg242322@gmail.com"
