from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = False
POSTGRESQL = False
HEROKU = True


def get_database():
    if SQLITE:
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    if POSTGRESQL:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'resizer',
            'USER': 'vova',
            'PASSWORD': 'kvb2371850',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    if HEROKU:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd7osur7ik4onnn',
            'USER': 'kwxlemlietkvma',
            'PASSWORD': '5f688d2f19c7d909143dd64526070ca442395e02007570f2f605391df5b5a6c3',
            'HOST': 'ec2-44-209-186-51.compute-1.amazonaws.com',
            'PORT': '5432',
        }
