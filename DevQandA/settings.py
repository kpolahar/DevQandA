# ================================================== #
#                   Settings File                    #
# ================================================== #

# -------------------- Imports --------------------- #
import os

# -------------------- Settings -------------------- #
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'c9_kg&sma@)y#jm312-7)jlkxbnz4li6l(^e5y7$tfo9-%arqe'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1:8000', '.kaetzi.com', '127.0.0.1']

INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'main',
                 ]

MIDDLEWARE = [
               'django.middleware.security.SecurityMiddleware',
               'django.contrib.sessions.middleware.SessionMiddleware',
               'django.middleware.common.CommonMiddleware',
               'django.middleware.csrf.CsrfViewMiddleware',
               'django.contrib.auth.middleware.AuthenticationMiddleware',
               'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
               'django.contrib.messages.middleware.MessageMiddleware',
               'django.middleware.clickjacking.XFrameOptionsMiddleware',
             ]

ROOT_URLCONF = 'DevQandA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'DevQandA.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/images')