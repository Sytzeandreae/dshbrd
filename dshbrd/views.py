# -*- coding: utf-8 -*-

from flask import render_template
from dshbrd import app


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

from api import views
