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

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
     msg = Message(subject, sender=sender, recipients=recipients)
     msg.body = text_body
     msg.html = html_body
#     mail.send(msg)
     thr = Thread(target=send_async_email, args=[current_app, msg])
     thr.start()


def inscription_notification(surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation ):
    send_email("[Mouv\'INSA] - L\'equipe vous remercie pour votre inscription %s!" % surnom,
               ADMIN[0],
               [email],
               render_template("/mails/inscription_email.txt",
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation ),
               render_template("/mails/inscription_email.html",
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation ))

def inscription_alert(inscrits, surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation ):
    send_email("[Mouv\'INSA] - NOUVEAU INSCRIT!!!!!! %s!" % categorie,
               ADMIN[0],
               [ADMIN[0]],
               render_template("/mails/inscription_alert.txt", inscrits=inscrits,
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation ),
               render_template("/mails/inscription_alert.html", inscrits=inscrits,
                               surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation ))

def sendInscriptionMailAndAlert(inscrits, surnom, email, categorie, nom, prenom, sexe, dateNaissance, poids, taille, cycle, annee, departement, filiere, position, affiliation):
    inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
    inscription_alert(inscrits="NOT DEFINED", surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )