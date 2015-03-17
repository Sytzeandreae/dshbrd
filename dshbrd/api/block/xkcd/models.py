# -*- coding: utf-8 -*-

from dshbrd.api.block.models import BaseBlockModel
from dshbrd.database import db


class XkcdBlock(BaseBlockModel, db.Model):
    url = 'http://www.xkcd.com/rss/xml'
