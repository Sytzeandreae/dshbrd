# -*- coding: utf-8 -*-

from flask.ext.restful import Resource


class RssBlockApi(Resource):
    def get(self):
        return {'hello': 'rss'}
