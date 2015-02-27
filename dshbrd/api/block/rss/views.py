# -*- coding: utf-8 -*-

from flask.ext.restful import Resource

from .models import RssBlock


class RssBlockApi(Resource):
    def get(self, id):
        block = RssBlock.get_by_id(id)
        return {
            'feed_url': block.feed_url,
            'name': block.block.name,
            'position': block.block.position
        }
