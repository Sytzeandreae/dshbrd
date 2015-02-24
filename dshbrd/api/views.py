# -*- coding: utf-8 -*-

from flask.ext.restful import Resource

from dshbrd.extensions import api


class UserApi(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(UserApi, '/users')
