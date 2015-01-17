#!/usr/bin/python
#  -*- coding: utf-8 -*-

import os
from wtforms import Form, TextField, DateField, validators, FloatField, IntegerField, SelectField
from werkzeug.utils import secure_filename

class ConfirmationForm(Form):
    lastname = TextField(u'Nom', validators=[validators.Optional(),
             validators.Length(min=2, max=25, message=u'La longeur doit être comprise entre 2 et 25 caractères.')])
    firstname = TextField(u'Prenom',[validators.Optional(),
             validators.Length(min=2, max=25, message=u'La longeur doit être comprise entre 2 et 25 caractères.')])
    birthdate = DateField(u'Date de Naissance', format='%d/%m/%Y',validators=[validators.Optional()])
    weight = FloatField(u'Poids (kg)',[validators.Optional(),
           validators.NumberRange(min=20, max=300, message=u'Le poids doit être compris entre 20kg et 300kg')])
    height = IntegerField(u'Taille (cm)', [validators.Optional(),
           validators.NumberRange(min=90, max=250, message=u'La taille doit être comprise entre 90cm et 250cm.')])
    sex = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), (u'Féminin', 'Feminin')],
                      validators=[validators.Optional()])

def updateProfil(form, person):
        person.lastname = form.lastname.data
        person.firstname = form.firstname.data
        person.weight = form.weight.data
        person.height = form.height.data
        person.birthdate = form.birthdate.data
        if form.sex.data == '':
            person.sex = 'Inconnu'
        else:
            person.sex = form.sex.data

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "/app/mouvinsa/static/images/"
MAX_IMAGE_SIZE = 1 * 1024 * 1024

def uploadImage(file, person):
            filename = secure_filename(file.filename)
            if checkExtImage(file.filename):
                extension = filename.rsplit('.',1)[1]
                filename = person.nickname+'_avatar.'+extension
                file_path = os.path.join(os.path.dirname(UPLOAD_FOLDER), filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                file.save(file_path)
                if checkSizeImage(file_path):
                    person.image = file_path.rsplit('/app/mouvinsa/', 1)[1]
                    return 1;
                else:
                    os.remove(file_path)
            return 0;

def checkExtImage(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def checkSizeImage(file_path):
    image_size = os.stat(file_path).st_size
    return image_size < MAX_IMAGE_SIZE
