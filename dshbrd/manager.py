# -*- coding: utf-8 -*-

from flask.ext.restful import Resource
from dshbrd.extensions import flask_api


class BlockApiManager(object):
    def __init__(self, app):
        self.app = app
        self._register_blocks()

    def _register_blocks(self):
        for name in self.app.config['REGISTERED_BLOCKS']:
            block = self._block_object(name)
            if block:
                self.register(block, name)

    def _block_object(self, name):
        try:
            mod = __import__('dshbrd.api.block.{0}.views'.format(name),
                             fromlist=[name])
            return getattr(mod, '{0}BlockApi'.format(name.capitalize()))
        except AttributeError:
            return None
        except ImportError:
            return None

    def register(self, block, name):
        if isinstance(block(), Resource):
            flask_api.add_resource(block, '/block/{0}/<int:id>'.format(name))
        else:
            raise TypeError('Block must be subclass of Block: {0}'.format(name))
