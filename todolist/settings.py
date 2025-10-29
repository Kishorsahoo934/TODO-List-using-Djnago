from pathlib import Path
import os
import firebase_admin
from firebase_admin import credentials, db
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i$@%sn#6ej%i=^od$j2ty%enp4kbcn6(k5lsmn2qct#p2bj*)j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # Allow all hosts for testing; restrict later in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
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

ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Folder for your HTML templates
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

WSGI_APPLICATION = 'todolist.wsgi.application'

# ---------------------------------
# DATABASE (Local PostgreSQL)
# ---------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'todo_django_app',
#         'USER': 'postgres',
#         'PASSWORD': '@Kishor789424',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

# ---------------------------------
# PASSWORD VALIDATION
# ---------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ---------------------------------
# INTERNATIONALIZATION
# ---------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------
# STATIC FILES
# ---------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ---------------------------------
# DEFAULT AUTO FIELD
# ---------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------------
# 🔥 FIREBASE CONFIGURATION 🔥
# ---------------------------------
# Use environment variable for Firebase credentials
try:
    if not firebase_admin._apps:  # Prevent re-initialization
        firebase_credentials = json.loads(os.environ['FIREBASE_CREDENTIALS'])
        cred = credentials.Certificate(firebase_credentials)
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://chromacart-fo6vc-default-rtdb.firebaseio.com'  # Replace with your database URL
        })
except Exception as e:
    print(f"Firebase initialization error: {e}")
