"""
Production Settings for Heroku
"""

from decouple import config

# If using in your own project, update the project namespace below
from ReservasVuelos.settings.local import *
import dj_database_url


DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

CORS_ALLOWED_ORIGINS = [config('CORS_ALLOWED_ORIGINS')]

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'] = dj_database_url.config(default=config('HEROKU_POSTGRESQL_PURPLE_URL'))