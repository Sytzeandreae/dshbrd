# -*- coding: utf-8 -*-

import requests
import xmltodict
from flask.ext.security import current_user

from .models import XkcdBlock
from ..views import AuthResource


class XkcdBlockApi(AuthResource):
    def get(self, id):
        feed = requests.get('http://xkcd.com/rss.xml')
        xkcd = xmltodict.parse(feed.text)

        if XkcdBlock.check_user(id, current_user.id):
            return xkcd['rss']['channel']['item'][0]
        else:
            return {
                'error': 'Access denied!'
            }
