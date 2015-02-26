# -*- coding: utf-8 -*-

from dshbrd.database import CRUDMixin, db
from sqlalchemy.ext.declarative import declared_attr


class Block(CRUDMixin, db.Model):
    name = db.Column(db.String(255))
    position = db.Column(db.Integer)
    blocktype = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('blocks'))


class BaseBlockModel(CRUDMixin, db.Model):
    @declared_attr
    def block_id(self):
        return db.Column(db.Integer, db.ForeignKey('block.id'))

    @declared_attr
    def block(self):
        return db.relationship('Block')
