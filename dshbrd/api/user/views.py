# -*- coding: utf-8 -*-

from flask.ext.security import current_user

from dshbrd.api.views import AuthResource
from dshbrd.auth.models import User
from dshbrd.extensions import flask_api


class UserApi(AuthResource):
    def get(self):
        user = User.get_by_id(current_user.id)
        return {
            'id': user.id,
            'email': user.email
        }

flask_api.add_resource(UserApi, '/user')
