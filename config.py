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
        '{engine}://{username}:{password}@{host}/{db}'.format(
            engine=environ.get('DB_ENGINE'),
            username=environ.get('DB_USER'),
            password=environ.get('DB_PASS'),
            host=environ.get('DB_HOST'),
            db=environ.get('DB_NAME')
        )
