#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

__author__ = 'marcomontalto'

#SYNC
from flask.ext.mail import Message
from flask import render_template
from app import mail
from config import ADMIN

#ASYNC
from threading import Thread
from flask import current_app
from decorators import async

from models import Person

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
     msg = Message(subject, sender=sender, recipients=recipients)
     msg.body = text_body
     msg.html = html_body
     mail.send(msg)
#     thr = Thread(target=send_async_email, args=[current_app, msg])
#     thr.start()


def mail_mot_de_passe_oublie(surnom, email, nouveau_mot_de_passe):
    send_email(u'[Mouv\'INSA] - %s demande de changement de mot de passe' %surnom,
               ADMIN[0], [email],
               render_template("/mails/mot_de_passe_oublie.txt",
                               surnom=surnom, nouveau_mot_de_passe=nouveau_mot_de_passe),
               render_template("/mails/mot_de_passe_oublie.html",
                               surnom=surnom, nouveau_mot_de_passe=nouveau_mot_de_passe))



def inscription_notification(surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation ):
    send_email("[Mouv\'INSA] - L\'equipe vous remercie pour votre inscription %s!" % surnom,
               ADMIN[0],
               [email],
               render_template("/mails/inscription_email_ret.txt",
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation),
               render_template("/mails/inscription_email_ret.html",
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation))

def inscription_alert(inscrits, surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation ):
    send_email("[Mouv\'INSA] - NOUVEAU INSCRIT!!!!!! %s!" % categorie,
               ADMIN[0],
               [ADMIN[0]],
               render_template("/mails/inscription_alert.txt", inscrits=inscrits,
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation),
               render_template("/mails/inscription_alert.html", inscrits=inscrits,
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation))

def sendInscriptionMailAndAlert(inscrits, surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation):
    inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation)
    inscription_alert(inscrits=inscrits, surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation)

def sendRappelRendezVous(surnom,email):
    send_email(u'[Mouv\'INSA] - %s viens retirer ton podomètre le mardi 3 février!' %surnom,
               ADMIN[0],
               [email],
               render_template("/mails/rappel_retirer_podometre.txt",
                               surnom=surnom),
               render_template("/mails/rappel_retirer_podometre.html",
                               surnom=surnom))

def sendMailGroupesDefinitifs(surnom, email, nomGroupe, numeroGroupe):
    send_email(u'[Mouv\'INSA] - Départ collectif le Jeudi 26 Février & Composition des groupes',
               ADMIN[0],
               [email],
               render_template("/mails/groupes_alert.txt",
                               surnom=surnom, nomGroupe=nomGroupe, numeroGroupe=numeroGroupe),
               render_template("/mails/groupes_alert.html",
                               surnom=surnom, nomGroupe=nomGroupe, numeroGroupe=numeroGroupe))

def sendMailDernierRappel(surnom, email):
    send_email(u'[Mouv\'INSA] - Etes-vous prêts à marcher?',
               ADMIN[0],
               [email],
               render_template("/mails/derniers_rappels_depart.txt",
                               surnom=surnom),
               render_template("/mails/derniers_rappels_depart.html",
                               surnom=surnom))

def sendMailConferenceSante(surnom, email):
    send_email(u'[Mouv\'INSA] - Conférence sur la Santé et le Lien Social',
               ADMIN[0],
               [email],
               render_template("/mails/conference_sante.txt",
                               surnom=surnom),
               render_template("/mails/conference_sante.html",
                               surnom=surnom))

def sendMailDoodle(surnom, email):
    send_email(u'[Mouv\'INSA] - Doodle conférence sur la Santé et le Lien Social',
               ADMIN[0],
               [email],
               render_template("/mails/doodle_conference.txt",
                               surnom=surnom),
               render_template("/mails/doodle_conference.html",
                               surnom=surnom))

def sendMailDoodlePot(surnom, email):
    send_email(u'[Mouv\'INSA] - Doodle Pot d\'arrivée',
               ADMIN[0],
               [email],
               render_template("/mails/pot_arrivee.txt",
                               surnom=surnom),
               render_template("/mails/pot_arrivee.html",
                               surnom=surnom))