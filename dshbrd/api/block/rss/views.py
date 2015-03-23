# -*- coding: utf-8 -*-

import requests
import xmltodict
from flask import abort
from flask.ext.restful import Resource
from flask.ext.security import current_user

from .models import RssBlock


class RssBlockApi(Resource):
    def get(self, id):
        if RssBlock.check_user(id, current_user.id):
            block = RssBlock.get_by_id(id)
            feed = requests.get(block.feed_url)
            return xmltodict.parse(feed.text)
        else:
            abort(403)
