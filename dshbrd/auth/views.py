# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, Blueprint
from flask.ext.security import login_required, LoginForm, \
    logout_user, login_user, current_user

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/', methods=['GET'])
@auth_bp.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(request.args.get('next') or '/')
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(request.args.get('next') or '/')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(request.args.get('next') or '/login')


@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')
