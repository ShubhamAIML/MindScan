from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-teen-mental-health-xgboost-2024'
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'predictor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'mental_health_app.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
    ]},
}]

WSGI_APPLICATION = 'mental_health_app.wsgi.application'

# ====== STATIC FILES CONFIGURATION (CRITICAL!) ======
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directory where Django looks for static files to collect
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'predictor', 'static')]

# Simple storage backend - WhiteNoise will handle caching
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Enable WhiteNoise autorefresh
WHITENOISE_AUTOREFRESH = not DEBUG

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Model path
MODEL_PATH = os.path.join(BASE_DIR, 'xgboost_depression_model.pkl')
