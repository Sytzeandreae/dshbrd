# -*- coding: utf-8 -*-

from flask.ext.restful import Resource

from dshbrd.extensions import flask_api


class UserApi(Resource):
    def get(self):
        return {'hello': 'world'}

#flask_api.add_resource(UserApi, '/users')
