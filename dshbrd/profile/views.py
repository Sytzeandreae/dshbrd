# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, Blueprint
from flask.ext.security import login_required

profile_bp = Blueprint(
    'profile', __name__, template_folder='templates', url_prefix='/profile'
)


@profile_bp.route('/')
@profile_bp.route('/index')
@login_required
def profile():
    return render_template('profile.html')
