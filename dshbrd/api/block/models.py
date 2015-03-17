# -*- coding: utf-8 -*-

from dshbrd.database import CRUDMixin, db
from sqlalchemy.ext.declarative import declared_attr


class Block(db.Model, CRUDMixin):
    name = db.Column(db.String(255))
    position = db.Column(db.Integer)
    blocktype = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('blocks'))

    @classmethod
    def get_by_user(cls, user):
        return cls.query.filter_by(user=user)


class BaseBlockModel(CRUDMixin):
    @classmethod
    def get_by_block_id(cls, block_id):
        return cls.query.filter_by(block_id=block_id)

    @declared_attr
    def block_id(self):
        return db.Column(db.Integer, db.ForeignKey('block.id'))

    @declared_attr
    def block(self):
        return db.relationship('Block')

    @classmethod
    def check_user(cls, block_id, user_id):
        block = cls.query.filter_by(bock_id=block_id)[0]
        return block.user_id == user_id
