# -*- coding: utf-8 -*-

from flask.ext.security import login_required
from flask.ext.restful import Resource


class AuthResource(Resource):
    decorators = [login_required]
