import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never'
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')


class DevelopmentConfig(Config):
    ...


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
