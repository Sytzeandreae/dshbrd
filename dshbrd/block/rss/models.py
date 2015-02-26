# -*- coding: utf-8 -*-

from dshbrd.block.models import BaseBlockModel
from dshbrd.database import db


class RssBlock(BaseBlockModel, db.Model):
    feed_url = db.Column(db.String(255))
