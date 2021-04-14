# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
from research_sys.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MONGODB_DATABASES = {
    "default": {
        "name": 'test',
        "host": '127.0.0.1',
        "username": 'admin',
        "password": '123456',
        "authentication_source": 'admin',
        "tz_aware": False,
    },
}
