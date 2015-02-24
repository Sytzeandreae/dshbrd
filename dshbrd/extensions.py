from flask.ext.restful import Api
api = Api()

from flask.ext.security import Security
security = Security()

from flask.ext.security import SQLAlchemyUserDatastore
users = SQLAlchemyUserDatastore(None, None, None)


def create_sql_alchemy_datastore(users_new, db, user, role):
    users_new = SQLAlchemyUserDatastore(db, user, role)
    return users_new


def create_api(api_new, app):
    api_new = Api(app)
    return api_new
