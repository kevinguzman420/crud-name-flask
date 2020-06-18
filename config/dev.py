# config/dev.py

from .default import *

APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = 'postgresql://user_db:pass_db@host:port/database_name'

