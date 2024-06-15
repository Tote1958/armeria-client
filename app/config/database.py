from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_migrate import Migrate


basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

USER_DB = os.environ.get('USER_DB')
PASS_DB = os.environ.get('PASS_DB')
URL_DB = os.environ.get('URL_DB')
NAME_DB = os.environ.get('NAME_DB')
PORT_DB = os.environ.get('PORT_DB')

PROD_DATABASE_URI = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'
DEV_DATABASE_URI = f'postgresql://{USER_DB}:{PASS_DB}@localhost:{PORT_DB}/{NAME_DB}'

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URI



class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = PROD_DATABASE_URI

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }

    return configuration[app];



#FULL_URL_DB = f'mariadb+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'  para maria db