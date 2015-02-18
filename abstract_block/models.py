# -*- coding: utf-8 -*-

from app import db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
