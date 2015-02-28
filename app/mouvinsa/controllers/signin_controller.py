#!/usr/bin/python
#  -*- coding: utf-8 -*-
from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField('email', [validators.Length(min=4, max=40)])
    password = PasswordField('password', [validators.DataRequired()])

class MdpForm(Form):
    email = StringField('email', [validators.Length(min=4, max=40)])