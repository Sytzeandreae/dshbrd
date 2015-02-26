# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, redirect
from flask.ext.security import roles_required

from ..auth import auth


@auth.route('/')
@roles_required('admin')
def admin_index():
    pass
