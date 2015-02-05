#!/usr/bin/python
#  -*- coding: utf-8 -*-
from werkzeug.debug import DebuggedApplication
from flask import Flask
from flask.ext.mail import Mail
from mouvinsa.config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.setdefault('SQLALCHEMY_DATABASE_URI', SQLALCHEMY_DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config.update(dict(
    DEBUG = True,
    # email server
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'mouvinsa.communication@gmail.com',
    MAIL_PASSWORD = '.1Mouvinsa=Mouv+insa',
))
mail = Mail(app)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


if app.debug:
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.secret_key = 'ty6739hjDyaidjdjdd6tef908c'

