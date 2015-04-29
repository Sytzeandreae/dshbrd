# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from dshbrd import create_app
from dshbrd import db

app = create_app()

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    app.run()


@manager.command
def initdb():
    from dshbrd.commands import initdb
    initdb()


@manager.command
def dropdb():
    from dshbrd.commands import dropdb
    dropdb()


@manager.command
def resetdb():
    from dshbrd.commands import resetdb
    resetdb()


@manager.command
def createdb():
    from dshbrd.commands import createdb
    createdb()

if __name__ == '__main__':
    manager.run(default_command='runserver')
