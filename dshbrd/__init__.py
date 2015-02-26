# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore

from dshbrd.extensions import flask_api, security
from dshbrd.database import db
from dshbrd.auth import auth
from dshbrd.auth.models import User, Role
from dshbrd.api import api_v1_bp
from dshbrd.manager import BlockManager


def create_app():
    app = Flask(__name__)
    env = os.environ.get('DSHBRD_CONFIG', 'Dev')
    app.config.from_object('config.{env}Config'.format(env=env))

    register_extensions(app)
    register_blueprints(app)

    BlockManager(app, flask_api)
    print flask_api.resources

    @app.route('/')
    def index():
        return 'hello_world'

    return app


def register_extensions(app):
    db.init_app(app)
    flask_api.init_app(api_v1_bp)
    users = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, users)


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(api_v1_bp)
