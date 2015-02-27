# -*- coding: utf-8 -*-

from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from .user import views
from .block import views
