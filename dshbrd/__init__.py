# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore

from dshbrd.extensions import flask_api, security
from dshbrd.database import db
from dshbrd.admin import admin_bp
from dshbrd.auth import auth_bp
from dshbrd.auth.models import User, Role
from dshbrd.api import api_v1_bp
from dshbrd.manager import BlockApiManager
from dshbrd.profile import profile_bp

users = SQLAlchemyUserDatastore(db, User, Role)


def create_app():
    app = Flask(__name__)
    env = os.environ.get('DSHBRD_CONFIG', 'Dev')
    app.config.from_object('config.{env}Config'.format(env=env))

    register_extensions(app)
    BlockApiManager(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    flask_api.init_app(api_v1_bp)
    security.init_app(app, users)


def register_blueprints(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_v1_bp)
    app.register_blueprint(profile_bp)
