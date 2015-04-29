# -*- coding: utf-8 -*-

from os import environ, path


class Config(object):
    BASE_PATH = path.dirname(__file__)

    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + path.join(BASE_PATH, 'db.sqlite')
    DEBUG = False

    HOST = '127.0.0.1'
    PORT = 5000

    SECRET_KEY = 'insert secret key here'

    REGISTERED_BLOCKS = [
        'reddit',
        'rss',
        'newrelic',
        'xkcd'
    ]


class DevConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    '''
    Config for staging.dshbrd.io
    '''
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = \
        '{engine}://{username}:{password}@{host}:{port}/{db}'.format(
            engine='postgresql',
            username=environ.get('RDS_USERNAME'),
            password=environ.get('RDS_PASSWORD'),
            host=environ.get('RDS_HOSTNAME'),
            db=environ.get('RDS_DB_NAME'),
            port=environ.get('RDS_PORT')
        )
