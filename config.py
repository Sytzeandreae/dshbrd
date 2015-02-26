# -*- coding: utf-8 -*-

from os import path


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
        'newrelic'
    ]


class DevConfig(Config):
    DEBUG = True
