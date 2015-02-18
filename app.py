# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

# Set the config
env = os.environ.get('DSHBRD_CONFIG', 'Dev')
app.config.from_object('config.{env}Config'.format(env=env))


# Create the database
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run()
