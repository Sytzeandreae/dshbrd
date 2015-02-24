# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, url_for, redirect
from flask.ext.security import SQLAlchemyUserDatastore, Security, \
    auth_token_required, roles_required

from dshbrd import app, db
from .auth.models import User, Role

users = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, users)

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/index')
@auth.route('/')
def index():
    return render_template('index.html')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/profile')
@roles_required('user')
def profile():
    return render_template('profile.html')
