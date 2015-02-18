#!/usr/bin/python
#  -*- coding: utf-8 -*-
from werkzeug.debug import DebuggedApplication
from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('mouvinsa.config')
mail = Mail(app)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


if app.debug:
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)