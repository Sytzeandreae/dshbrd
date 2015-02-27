# -*- coding: utf-8 -*-

from flask.ext.restful import Resource


class NewrelicBlockApi(Resource):
    def get(self):
        return {'hello': 'newrelic'}
