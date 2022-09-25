from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = True
POSTGRESQL = False


def get_database():
    if SQLITE:
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    else:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'resizer',
            'USER': 'vova',
            'PASSWORD': 'kvb2371850',
            'HOST': 'localhost',
            'PORT': '5432',
        }