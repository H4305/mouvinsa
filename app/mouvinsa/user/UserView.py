#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
from wtforms.fields.simple import SubmitField
from flask import render_template
from flask.ext.wtf.file import FileField
from flask.ext.wtf import Form
from wtforms import FloatField, PasswordField, SelectField, DateField, validators
from mouvinsa.controllers.inscription_controller import \
    messagePassword, messageLongueur4_25, CHOIX_SEXE, messagePoids, messageTaille

__author__ = 'vcaen'

LABEL_HEIGHT = u'Taille (cm)'
LABEL_WEIGHT = u'Poids (kg)'
LABEL_SEX = u'Sexe '
LABEL_BIRTHDATE = u'Né(e) le'
LABEL_CONF_PASS = u'Confirmez le mot de passe'
LABEL_MOTDEPASSE = u'Mot de Passe'
LABEL_IMAGE = u'Photo de profil'
LABEL_SUBMIT = u'Valider les changements'

def display_profil(person):
    """
    Display the home page for the user
    :param person: the user concerned by the data
    :return: the corresponding page template
    """
    return render_template('person/main.html', person=person)

def display_settings(person, form):
    """
    Display the settings for the user
    :param request: the request made for the settings
    :param person: the user concerned by the settings
    :return: the populated template.
    """
    return render_template('reglages/main.html', person=person, form=form)

def generate_setting_form(request, person):
    """
    genrate the settings for the user
    :param request: the request made for the settings
    :param person: the user concerned by the settings
    :return: the populated template.
    """
    if request.method == 'POST':
        form = UserForm(request.form, obj=person)
        form.validate()
    else:
        form = UserForm(obj=person)
    return form


class UserForm(Form):
    image = FileField( LABEL_IMAGE, [validators.regexp(u'.*\.(jpg|png)$'), validators.Optional()])
    password = PasswordField(LABEL_MOTDEPASSE, [
        validators.Optional(),
        validators.EqualTo('confirm', message=messagePassword),
        validators.Length(min=4, max=25, message=messageLongueur4_25)
    ])
    confirm = PasswordField(LABEL_CONF_PASS)
    birthdate = DateField(LABEL_BIRTHDATE, format='%d/%m/%Y', validators=[validators.Optional()])
    sex = SelectField(LABEL_SEX, choices=CHOIX_SEXE)
    weight = FloatField(LABEL_WEIGHT,
                        [validators.Optional(), validators.NumberRange(min=20, max=300, message=messagePoids)])
    height = FloatField(LABEL_HEIGHT,
                        [validators.Optional(), validators.NumberRange(min=90, max=250, message=messageTaille)])
    submit = SubmitField(LABEL_SUBMIT)




