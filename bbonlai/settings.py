import os
import dj_database_url
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'hs!a_t--vygd_nqd^vf9ru4svzd-ztp(z3&wg*dd8v_j&)zi0t')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'ppco2.apps.Ppco2Config',
    'formtools',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'bbonlai.urls'

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

WSGI_APPLICATION = 'bbonlai.wsgi.application'

if os.environ.get('DATABASE_URL'):
    heroku = dj_database_url.config(default=os.environ['DATABASE_URL'])
# else:  # when production, remove the else clause.
#     heroku = {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "dc5f2ms0dvvqlb",
#         "USER": "iyiyqqhfvwmalt",
#         "PASSWORD": "1296e7228d3cf7d03cb10c71a5a206f999d43a36bbc8f1cbbf6fdcc02a5128cc",
#         "HOST": "ec2-18-235-97-230.compute-1.amazonaws.com",
#         "PORT": "5432",
#     }


DATABASES = {
    "default": heroku
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Phnom_Penh'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
django_heroku.settings(locals())
