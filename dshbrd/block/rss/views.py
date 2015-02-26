# -*- coding: utf-8 -*-

from flask.ext.restful import Resource


class BlockApi(Resource):
    def get(self):
        return {'hello': 'rss'}
