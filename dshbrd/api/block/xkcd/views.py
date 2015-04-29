# -*- coding: utf-8 -*-

import requests
import HTMLParser
from bs4 import BeautifulSoup
from flask import abort
from flask.ext.security import current_user

from .models import XkcdBlock
from ..views import AuthResource
from ..models import Block


class XkcdBlockApi(AuthResource):
    def get(self, id):
        if XkcdBlock.check_user(id, current_user.id):
            feed = requests.get('http://xkcd.com/rss.xml')
            h = HTMLParser.HTMLParser()
            t = h.unescape(feed.text)

            # Extract the url, alt text and the title from the image
            soup = BeautifulSoup(t)
            item = soup.rss.channel.item

            return {
                'img': {
                    'url': item.description.img.get('src'),
                    'alt': item.description.img.get('alt'),
                    'title': item.description.img.get('title')
                },
                'title': item.title.get_text(),
                'url': item.link.get_text()
            }
        else:
            abort(403)

    def put(self, id):
        if XkcdBlock.check_user(id, current_user.id):
            pass
        else:
            abort(403)

    def post(self):
        pass

    def delete(self, id):
        if XkcdBlock.check_user(id, current_user.id):
            xb = XkcdBlock.get_by_id(id)
            b = Block.get_by_id(xb.block_id)

            xb.delete()
            b.delete()

            return {
                'success': True
            }
        else:
            abort(403)
