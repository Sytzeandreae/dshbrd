# -*- coding: utf-8 -*-

import requests
import xmltodict
from flask import abort
from flask.ext.security import current_user

from .models import RssBlock
from ..views import AuthResource
from ..models import Block


class RssBlockApi(AuthResource):
    def get(self, id):
        if RssBlock.check_user(id, current_user.id):
            block = RssBlock.get_by_id(id)
            feed = requests.get(block.feed_url)
            return xmltodict.parse(feed.text)
        else:
            abort(403)

    def put(self, id, form):
        if RssBlock.check_user(id, current_user.id):
            pass
        else:
            abort(403)

    def post(self, form):
        pass

    def delete(self, id):
        if RssBlock.check_user(id, current_user.id):
            rb = RssBlock.get_by_id(id)
            b = Block.get_by_id(rb.block_id)

            rb.delete()
            b.delete()
        else:
            abort(403)
