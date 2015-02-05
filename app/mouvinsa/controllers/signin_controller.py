#!/usr/bin/python
#  -*- coding: utf-8 -*-
from wtforms import Form,TextField, PasswordField, validators

class LoginForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])



class MdpForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=25)])