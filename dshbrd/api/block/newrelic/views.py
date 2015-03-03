# -*- coding: utf-8 -*-

from flask.ext.restful import Resource

from .models import NewrelicBlock


class NewrelicBlockApi(Resource):
    def get(self, id):
        block = NewrelicBlock.get_by_id(id)
        return {
            'apikey': block.api_key
        }
