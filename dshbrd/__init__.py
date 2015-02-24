# -*- coding: utf-8 -*-

import os
from flask import Flask

from dshbrd.extensions import api, users, create_api, \
    create_sql_alchemy_datastore, security
from dshbrd.database import db
from dshbrd.auth import auth
from dshbrd.auth.models import User, Role
from dshbrd.api import api_v1_bp


def create_app():
    app = Flask(__name__)
    env = os.environ.get('DSHBRD_CONFIG', 'Dev')
    app.config.from_object('config.{env}Config'.format(env=env))

    register_extensions(app)
    register_blueprints(app)

    @app.route('/')
    def index():
        return 'hello_world'

    return app


def register_extensions(app):
    db.init_app(app)
    create_api(api, api_v1_bp)
    create_sql_alchemy_datastore(users, db, User, Role)
    security.init_app(app, users)


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(api_v1_bp)
