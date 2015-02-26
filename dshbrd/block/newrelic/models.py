# -*- coding: utf-8 -*-

from dshbrd.block.models import BaseBlockModel
from dshbrd.database import db


class NewRelicBlock(BaseBlockModel, db.Model):
    api_key = db.Column(db.String(255))
