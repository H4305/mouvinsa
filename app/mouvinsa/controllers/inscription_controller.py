#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8
from wtforms import Form, TextField, FloatField, PasswordField, SelectField, DateField, validators
from mouvinsa.utils import PassHash

# import uuid
# from hashlib import sha256
# from mouvinsa.utils import passHash

# def hash_password(password):
# salt = uuid.uuid4().hex
# return sha256(salt.encode() + password.encode()).hexdigest() + \
#         ':' + salt

CHOIX_SEXE = [('', ''),
              ('Masculin', 'Masculin'),
              (u'Feminin', u'Feminin')]

CHOIX_CATEGORIE = [('Etudiant', 'Etudiant'),
                   ('Enseignant-Chercheur', 'Enseignant-Chercheur'),
                   ('Personnel IATOS', 'Personnel IATOS')]

CHOIX_DEPARTEMENT = [('', ''),
                     ('BB', 'BB'),
                     ('BIM', 'BIM'),
                     ('GE', 'GE'),
                     ('GI', 'GI'),
                     ('GCU', 'GCU'),
                     ('GEN', 'GEN'),
                     ('GMC', 'GMC'),
                     ('GMD', 'GMD'),
                     ('GMPP', 'GMPP'),
                     ('IF', 'IF'),
                     ('SGM', 'SGM'),
                     ('TC', 'TC')]

CHOIX_CYCLE = [('', ''),
               ('Premier', 'Premier'),
               ('Second', 'Second')]

CHOIX_FILIERE = [('', ''),
                 ('Internationale', 'Internationale'),
                 ('Classique', 'Classique'),
                 ('PCE', 'PCE'),
                 ('FAS', 'FAS'),
                 ('SHN', 'SHN')]

CHOIX_ANNEE = [
    ('', ''),
    (u'Premiere', u'Premiere'),
    (u'Deuxieme', u'Deuxieme'),
    (u'Troisieme', u'Troisieme'),
    (u'Quatrieme', u'Quatrieme'),
    (u'Cinquieme', u'Cinquieme')
]

messageObligatoire = u'Ce champs est obligatoire. Veuillez le remplir.'
messageEmail = u'Les deux emails doivent correspondre. Veuillez réessayer.'
messageLongueur2_25 = u'La longueur doit être comprise entre 2 et 25 caractères.'
messagePassword = u'Les 2 mots de passe doivent correspondre.  Veuillez réessayer.'
messageLongueur4_25 = u'La longueur doit être comprise entre 4 et 25 caractères.'
messagePoids = u'Le poids doit être compris entre 20 kg et 300 kg'
messageTaille = u'La taille doit être comprise entre 90 cm et 250 cm.'
messageLongueur3_100 = u'La longueur doit être comprise entre 3 et 100 caractères.'
MESSAGE_CHAMPS_OBLIGATOIRE = 'Ce champs est obligatoire. Veuillez le remplir.'


class InscriptionForm(Form):
    email = TextField(u'Email', [validators.Required(message=messageObligatoire),
                                 validators.EqualTo('confirmEmail', message=messageLongueur2_25)])
    confirmEmail = TextField(u'Confirmez votre email',
                             [validators.Required(message=MESSAGE_CHAMPS_OBLIGATOIRE)])
    surnom = TextField(u'Pseudonyme', [validators.Required(message=messageObligatoire),
                                       validators.Length(min=2, max=25, message=messageLongueur2_25)])
    nom = TextField(u'Nom', [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
    prenom = TextField(u'Prénom',
                       [validators.Optional(), validators.Length(min=2, max=25, message=messageLongueur2_25)])
    categorie = SelectField(u'Catégorie', [validators.Required(message=messageObligatoire)], choices=CHOIX_CATEGORIE)
    annee = SelectField(u'Année', choices=CHOIX_ANNEE)
    cycle = SelectField(u'Cycle', choices=CHOIX_CYCLE)
    filiere = SelectField(u'Filière', choices=CHOIX_FILIERE)
    departement = SelectField(u'Département', choices=CHOIX_DEPARTEMENT)
    password = PasswordField(u'Mot de Passe', [
        validators.Required(message=messageObligatoire),
        validators.EqualTo('confirm', message=messagePassword),
        validators.Length(min=4, max=25, message=messageLongueur4_25)
    ])
    confirm = PasswordField(u'Confirmez le mot de passe', [validators.Required(message=messageObligatoire)])
    dateNaissance = DateField(u'Né(e) le', format='%d/%m/%Y', validators=[validators.Optional()])
    sexe = SelectField(u'Sexe ', choices=CHOIX_SEXE)
    poids = FloatField(u'Poids (kg)',
                       [validators.Optional(), validators.NumberRange(min=20, max=300, message=messagePoids)])
    hauteur = FloatField(u'Taille (cm)',
                         [validators.Optional(), validators.NumberRange(min=90, max=250, message=messageTaille)])
    position = TextField(u'Position',
                         [validators.Optional(), validators.Length(min=3, max=100, message=messageLongueur3_100)])
    affiliation = TextField(u'Affiliation',
                            [validators.Optional(), validators.Length(min=3, max=100, message=messageLongueur3_100)])


def createStudent(form, student):
    student.firstname = form.prenom.data
    student.lastname = form.nom.data
    student.nickname = form.surnom.data
    student.password = PassHash.hash_password(form.password.data)
    student.email = form.email.data
    if form.sexe.data == '':
        student.sex = 'Inconnu'
    else:
        student.sex = form.sexe.data
    student.category = 'etudiant'
    student.year = form.annee.data
    student.cycle = form.cycle.data
    if form.cycle.data == 'Premier':
        student.branch = form.filiere.data
    else:
        student.branch = form.departement.data
    student.birthdate = form.dateNaissance.data
    student.weight = form.poids.data
    student.height = form.hauteur.data
    student.etat = "PREREGISTERED"


def createEmployee(form, employee):
    employee.firstname = form.prenom.data
    employee.lastname = form.nom.data
    employee.nickname = form.surnom.data
    employee.password = PassHash.hash_password(form.password.data)
    employee.email = form.email.data
    if form.sexe.data == '':
        employee.sex = 'Inconnu'
    else:
        employee.sex = form.sexe.data
    employee.birthdate = form.dateNaissance.data
    if form.categorie.data == 'Enseignant-Chercheur':
        employee.category = 'enseignant'
    else:
        employee.category = 'iatos'
    employee.weight = form.poids.data
    employee.height = form.hauteur.data
    employee.etat = "PREREGISTERED"
    employee.affiliation = form.affiliation.data
    employee.position = form.position.data