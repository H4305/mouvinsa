#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
import os
from werkzeug.utils import secure_filename, redirect
from mouvinsa.app import app
from wtforms.fields.simple import SubmitField
from flask import render_template, request, url_for, send_from_directory
from flask.ext.wtf.file import FileField
from flask.ext.wtf import Form
from wtforms import FloatField, PasswordField, SelectField, DateField, validators, StringField
from mouvinsa.controllers.inscription_controller import \
    messagePassword, messageLongueur4_25, CHOIX_SEXE, messagePoids, messageTaille, messageLongueur2_25, CHOIX_ANNEE, \
    CHOIX_CYCLE, CHOIX_FILIERE, CHOIX_DEPARTEMENT, messageLongueur3_100

LABEL_AFFILIATION = u'Affiliation'
LABEL_POSITION = u'Position'
LABEL_BRANCH = u'Département'
LABEL_CYCLE = u'Cycle'
LABEL_YEAR = u'Année'
LABEL_FIRSTNAME = u'Prénom'
LABEL_LASTNAME = u'Nom'
LABEL_GOAL = u'Objectif personnel (pas)'
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
    goal = FloatField(LABEL_GOAL,[validators.Optional()])
    password = PasswordField(LABEL_MOTDEPASSE, [
        validators.Optional(),
        validators.EqualTo('confirm', message=messagePassword),
        validators.Length(min=4, max=25, message=messageLongueur4_25)
    ])
    lastname = StringField(LABEL_LASTNAME, [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
    firstname = StringField(LABEL_FIRSTNAME,
                       [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
    confirm = PasswordField(LABEL_CONF_PASS)
    birthdate = DateField(LABEL_BIRTHDATE, format='%d/%m/%Y', validators=[validators.Optional()])
    sex = SelectField(LABEL_SEX, choices=CHOIX_SEXE)
    weight = FloatField(LABEL_WEIGHT,
                        [validators.Optional(), validators.NumberRange(min=20, max=300, message=messagePoids)])
    height = FloatField(LABEL_HEIGHT,
                        [validators.Optional(), validators.NumberRange(min=90, max=250, message=messageTaille)])
    submit = SubmitField(LABEL_SUBMIT)
    year = SelectField(LABEL_YEAR, choices=CHOIX_ANNEE)
    cycle = SelectField(LABEL_CYCLE, choices=CHOIX_CYCLE)
    branch = SelectField(LABEL_BRANCH, choices=CHOIX_DEPARTEMENT)
    position = StringField(LABEL_POSITION,
                         [validators.Optional(), validators.Length(min=3, max=100, message=messageLongueur3_100)])
    affiliation = StringField(LABEL_AFFILIATION,
                            [validators.Optional(), validators.Length(min=3, max=100, message=messageLongueur3_100)])


@app.route('/uploads/<filename>')
def display_picture(filename):
    """
    Display an uploaded picture
    :param filename: the filename insdide the upload directory
    :return: the picture
    """
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        # Check if the profile picture exists
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename)
    else:
        # Or return the default picture
        return redirect(url_for('static', filename='images/person/defaultm.png'))
