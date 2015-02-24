# -*- coding: utf-8 -*-

import os
from flask import Flask, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    env = os.environ.get('DSHBRD_CONFIG', 'Dev')
    app.config.from_object('config.{env}Config'.format(env=env))
    return app

# Initialize the application
app = create_app()

# Initialize the extensions
db = SQLAlchemy(app)

from . import auth
