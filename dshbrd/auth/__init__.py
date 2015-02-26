# -*- coding: utf-8 -*-

from flask import Blueprint

auth = Blueprint(
    'admin', __name__, template_folder='templates', url_prefix='/admin'
)

import views
