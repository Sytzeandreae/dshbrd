# -*- coding: utf-8 -*-


def initdb():
    from dshbrd.database import db
    print("Creating database tables")
    db.create_all()
    print("Database tables created!")


def dropdb():
    from dshbrd.database import db
    print("Deleting database tables")
    db.drop_all()
    print("Database deleted :(")


def resetdb(noinput=False):
    dropdb()
    initdb()
    initauth(noinput)


def request_input(question, default=None):
    try:
        value = "[{v}]".format(v=default) if default else ''
        return raw_input("{question}{default}:".format(
            question=question,
            default=value
        ))
    except ValueError:
        pass


def initauth(noinput):
    from flask.ext.security.utils import encrypt_password
    from dshbrd import users

    # Create the roles
    roles = ['admin']
    for role in roles:
        users.create_role(name=role, description=role)
    users.commit()
    print("Created roles {roles}".format(roles=roles))

    # Create a new user
    print("Started user creation process")
    if noinput:
        email = "info@dshbrd.io"
        password = "test"
    else:
        email = request_input("Email Address", "info@dshbrd.io")
        password = request_input("Password", "test")
    user = users.create_user(email=email, password=encrypt_password(password))
    users.add_role_to_user(user=user, role='admin')
    users.commit()
    print("Created user {0}".format(email))


def createdb(noinput=False):
    initdb()
    initauth(noinput)
