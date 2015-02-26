# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, Blueprint
from flask.ext.security import roles_required

admin_bp = Blueprint(
    'admin', __name__, template_folder='templates', url_prefix='/admin'
)


@admin_bp.route('/', methods=['GET'])
@admin_bp.route('/index', methods=['GET'])
@roles_required('admin')
def index():
    return render_template('index.html')
