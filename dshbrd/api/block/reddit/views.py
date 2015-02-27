# -*- coding: utf-8 -*-

from flask.ext.restful import Resource


class RedditBlockApi(Resource):
    def get(self):
        return {
            'hello': 'reddit'
        }
