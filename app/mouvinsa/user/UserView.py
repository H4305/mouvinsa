#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
__author__ = 'vcaen'
from flask import render_template
from wtforms import Form, TextField, FloatField, PasswordField, SelectField, DateField, validators
from mouvinsa.controllers.inscription_controller import \
    messageObligatoire, messagePassword, messageLongueur4_25, CHOIX_SEXE, messagePoids, messageTaille


def display_settings(request, person):
    form = UserForm(obj=person)
    return render_template('reglages/main.html', person=person, form=form)


class UserForm(Form):
    password = PasswordField(u'Mot de Passe', [
        validators.Required(message=messageObligatoire),
        validators.EqualTo('confirm', message=messagePassword),
        validators.Length(min=4, max=25, message=messageLongueur4_25)
    ])
    confirm = PasswordField(u'Confirmez le mot de passe', [validators.Required(message=messageObligatoire)])
    birthdate = DateField(u'Né(e) le', format='%d/%m/%Y', validators=[validators.Optional()])
    sex = SelectField(u'Sexe ', choices=CHOIX_SEXE)
    weight = FloatField(u'Poids (kg)',
                        [validators.Optional(), validators.NumberRange(min=20, max=300, message=messagePoids)])
    height = FloatField(u'Taille (cm)',
                        [validators.Optional(), validators.NumberRange(min=90, max=250, message=messageTaille)])

