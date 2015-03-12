# -*- coding: utf-8 -*-

import requests
import xmltodict
from flask.ext.restful import Resource

from .models import RssBlock


class RssBlockApi(Resource):
    def get(self, id):
        block = RssBlock.get_by_id(id)
        feed = requests.get(block.feed_url)
        return xmltodict.parse(feed.text)
