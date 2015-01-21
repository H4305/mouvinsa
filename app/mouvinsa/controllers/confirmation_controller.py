#!/usr/bin/python
#  -*- coding: utf-8 -*-

import os
from wtforms import Form, TextField, DateField, validators, FloatField, IntegerField, SelectField
from werkzeug.utils import secure_filename

class ConfirmationForm(Form):
    lastname = TextField(u'Nom', validators=[validators.Optional(),
             validators.Length(min=2, max=25, message=u'La longueur doit être comprise entre 2 et 25 caractères.')])
    firstname = TextField(u'Prenom',[validators.Optional(),
             validators.Length(min=2, max=25, message=u'La longueur doit être comprise entre 2 et 25 caractères.')])
    birthdate = DateField(u'Date de Naissance', format='%d/%m/%Y',validators=[validators.Optional()])
    weight = FloatField(u'Poids (kg)',[validators.Optional(),
           validators.NumberRange(min=20, max=300, message=u'Le poids doit être compris entre 20kg et 300kg')])
    height = IntegerField(u'Taille (cm)', [validators.Optional(),
           validators.NumberRange(min=90, max=250, message=u'La taille doit être comprise entre 90cm et 250cm.')])
    sex = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), (u'Féminin', 'Feminin')],
                      validators=[validators.Optional()])
    year = SelectField(u'Année', choices=[('', ''), (u'Premiere', u'Premiere'), (u'Deuxieme', u'Deuxieme'), (u'Troisieme', u'Troisieme'), (u'Quatrieme', u'Quatrieme'), (u'Cinquieme', u'Cinquieme')])
    cycle = SelectField(u'Cycle', choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')])
    branch = SelectField(u'Filière', choices=[('', ''), ('Internationale','Internationale'), ('Classique', 'Classique'), ('PCE','PCE'), ('FAS','FAS'), ('SHN','SHN')])
    department = SelectField(u'Département', choices=[('',''), ('BB', 'BB'), ('BIM', 'BIM'), ('GE', 'GE'), ('GI', 'GI'), ('GCU', 'GCU'), ('GEN', 'GEN'), ('GMC', 'GMC'), ('GMD', 'GMD'), ('GMPP', 'GMPP'), ('IF', 'IF'), ('SGM', 'SGM'), ('TC', 'TC')])
    position = TextField(u'Position', [validators.Optional(), validators.Length(min=3, max=100,  message=u'La longueur doit être comprise entre 3 et 100 caractères.')])
    affiliation = TextField(u'Affiliation', [validators.Optional(), validators.Length(min=3, max=100,  message=u'La longueur doit être comprise entre 3 et 100 caractères.')])

def updateProfil(form, person):
    if person.category == 'etudiant':
        person.year = form.year.data
        person.cycle = form.cycle.data
        person.branch = form.branch.data
        person.department = form.branch.data
    elif person.category == 'enseignant':
        person.department = form.branch.data
        person.position = form.position.data
        person.affiliation = form.affiliation.data
    else:
        person.position = form.position.data
        person.affiliation = form.affiliation.data
    person.lastname = form.lastname.data
    person.firstname = form.firstname.data
    person.weight = form.weight.data
    person.height = form.height.data
    person.birthdate = form.birthdate.data
    if form.sex.data == '':
        person.sex = 'Inconnu'
    else:
        person.sex = form.sex.data

# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "/app/mouvinsa/static/images/"
# MAX_IMAGE_SIZE = 1 * 1024 * 1024

def uploadImage(file, person):
            filename = secure_filename(file.filename)
            # if checkExtImage(file.filename):
            extension = filename.rsplit('.',1)[1]
            filename = person.nickname+'_avatar.'+extension
            file_path = os.path.join(os.path.dirname(UPLOAD_FOLDER), filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            file.save(file_path)
            # if checkSizeImage(file_path):
            person.image = file_path.rsplit('/app/mouvinsa/', 1)[1]
            # return 1
            # else:
            #     os.remove(file_path)
            # return 0

# def checkExtImage(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# def checkSizeImage(file_path):
#     image_size = os.stat(file_path).st_size
#     return image_size < MAX_IMAGE_SIZE
