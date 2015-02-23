#!/usr/bin/python
#  -*- coding: utf-8 -*-
import os
from werkzeug.debug import DebuggedApplication
from flask import Flask
from flask.ext.mail import Mail
from config import UPLOAD_FOLDER
from mouvinsa import config

app = Flask(__name__)
app.config.from_object('mouvinsa.config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.UPLOAD_MAX_SIZE
mail = Mail(app)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


if app.debug:
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)