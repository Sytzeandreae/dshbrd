# -*- coding: utf-8 -*-

from dshbrd.block.models import BaseBlockModel
from dshbrd.database import db


class RedditBlock(BaseBlockModel, db.Model):
    subreddit = db.Column(db.String(255))
