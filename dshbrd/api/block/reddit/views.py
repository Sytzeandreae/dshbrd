# -*- coding: utf-8 -*-

from flask.ext.restful import Resource

from .models import RedditBlock


class RedditBlockApi(Resource):
    def get(self):
        block = RedditBlock.get_by_id(id)
        return {
            'subreddit': block.subreddit,
            'name': block.block.name,
            'position': block.block.position
        }
