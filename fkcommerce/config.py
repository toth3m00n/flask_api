import os
from sqlalchemy.engine.url import URL

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never'
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')


class DevelopmentConfig(Config):
    url_object = URL.create(
        "postgresql+psycopg2",
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )
    SQLALCHEMY_DATABASE_URI = url_object
    
    # SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
