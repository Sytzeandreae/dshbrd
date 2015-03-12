# -*- coding: utf-8 -*-

from flask.ext.security import current_user

from sqlalchemy import inspect

from dshbrd.api.block.models import Block
from dshbrd.extensions import flask_api
from dshbrd.api.views import AuthResource

from dshbrd.api.block.rss.views import RssBlockApi


class UserBlockApi(AuthResource):
    _loaded_models = {}

    def get(self):
        '''
        Get all the blocks registered to the current_user
        '''
        block_list = []
        blocks = Block.get_by_user(current_user)

        for block in blocks:
            # First, import the right model
            if block.blocktype in self._loaded_models:
                model = self._loaded_models[block.blocktype]
            else:
                model = self._get_model_object(block.blocktype)

            # Get the right object
            b = model.get_by_block_id(block.id)

            block_list.append({
                'block_id': block.id,
                'block_name': block.name,
                'block_type': block.blocktype,
                'block_position': block.position,
                'block_specifics': self._get_block_specifics(model, b)
            })
        return block_list

    def _get_block_specifics(self, model, value):
        '''
        Return a dictionary containing the specific values for a block
        @param model The model class
        @param value The model instance
        @return dict
        '''
        mapper = inspect(model)
        specifics = {}

        # Loop through the attributes of the model class
        # adding all attributes to a dictionary except for
        # the attributes block and block_id, we already know
        # these in the caller of this function.
        for column in mapper.attrs:
            c = str(column).split('.')
            if not c[1] == 'block' and not c[1] == 'block_id':
                specifics[c[1]] = getattr(value[0], c[1])
        return specifics

    def _get_model_object(self, name):
        '''
        Attempt to import a class based on the name parameter.
        It will look in the path: dshbrd.api.block.{name}.models
        for the class {Name}Block (name is capitalized).

        Once the class has been imported, store it in a dictionary
        so we don't have to import it again.

        If the class can't be found, return None

        @param name Part of the name
        @return the class or None if it can't be found
        '''
        try:
            mod = __import__(
                'dshbrd.api.block.{0}.models'.format(name),
                fromlist=[name]
            )
            model = getattr(
                mod, '{0}Block'.format(name.capitalize())
            )
            self._loaded_models[name] = model
            return model
        except (AttributeError, ImportError):
            return None

flask_api.add_resource(UserBlockApi, '/user/blocks')
