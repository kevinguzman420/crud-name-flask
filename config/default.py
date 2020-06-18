# config/default.py

SECRET_KEY = '8bfb6b0c227159bfa9947cfc7634fbe5869b0124'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# App enviroments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''