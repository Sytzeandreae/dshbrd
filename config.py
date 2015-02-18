# -*- coding: utf-8 -*-

from os import path


class Config(object):
    BASE_PATH = path.dirname(__file__)

    DEBUG = False

    HOST = '127.0.0.1'
    PORT = 5000

    SECRET_KEY = 'insert secret key here'


class DevConfig(Config):
    DEBUG = True
