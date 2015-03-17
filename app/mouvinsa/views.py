#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8


#-------------------Imports
from flask import render_template, request, flash, url_for, redirect, jsonify
from app import app
from controllers.signin_controller import LoginForm, MdpForm
from models import db, Person, Group, Steps, FitnessInfo, Student, Employee, Questions
from emails import mail_mot_de_passe_oublie, sendInscriptionMailAndAlert, sendMailConferenceSante
from mouvinsa.user import UserController
from mouvinsa.utils.passHash import hash_password
from mouvinsa.user.UserManager import loginmouv
from mouvinsa.user.SessionManager import saveInSession, checkSession, clearSession, getPersonFromSession, login_required
from mouvinsa.utils.mdp import generate_mdp
from mouvinsa.controllers.inscription_controller import *
from datetime import date, timedelta
import datetime, time
import operator
from sqlalchemy import desc
#-------------------End Imports


#-------------------Filters

#Template filter
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%H:%M / %d/%m/%Y'):
    return value.strftime(format)

#-------------------End Filters


#--------------------Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', error=e)

#--------------------End error handlers


#--------------------Web Pages

#Home
@app.route('/', methods=['GET', 'POST'])
def home():
    person = getPersonFromSession()
    index = 'yes'
    groups = Group.query.order_by(desc(Group.stepSum))
    nbPasTotales = 0
    distanceTotale = 0
    for group in groups:
        nbPasTotales = nbPasTotales + group.stepSum
        distanceTotale = (distanceTotale + group.distance)

    distanceTotaleRound = round(distanceTotale/1000, 2)
    toursTerre = round(distanceTotaleRound/40075, 2)
    distanceTotale = int(distanceTotale/1000)
    return render_template('/accueil/index.html', person=person, index=index, groups=groups, nbPasTotales="{:,}".format(nbPasTotales), distanceTotale="{:,}".format(distanceTotale), toursTerre=toursTerre)


#A Propos
@app.route('/apropos', methods=['GET', 'POST'])
def apropos():
    person = getPersonFromSession()
    return render_template('/a propos/main.html', person=person)

# Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if checkSession() is False:
            return render_template('auth/signin.html')
        else:
            return redirect(url_for('home'))

    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data

            if email.count('@') != 0:
                flash(u'L\'email entré est incorrect', 'error_login')
                return render_template('auth/signin.html')
            email += "@insa-lyon.fr"

            password = form.password.data
            objeet, error = loginmouv(email, password)

            if objeet is None:
                if error == 1:
                    problem = u'L\'utilisateur ' + email + u'n\'existe pas.'
                    flash(problem, 'error_login')
                    page = "auth/signin.html"
                elif error == 2:
                    problem = u'Connexion refusé'
                    flash(problem, 'error_login')
                    page = "auth/signin.html"
            else:
                saveInSession(objeet.id)
                problem = u'Connexion ok'
                flash(problem, 'error_login')


                return redirect(url_for('personnel'))

            return render_template(page, form=form)

        else:
            problem = u'Connexion refusé'
            flash(problem, 'error_login')
            return render_template('auth/signin.html')


# Mot de passe oublie
@app.route('/forgetpassword/', methods=['GET', 'POST'])
def forgetpassword():
    if request.method == 'GET':
        return render_template('auth/forgetpassword.html')
    elif request.method == 'POST':
        form = MdpForm(request.form)
        if form.validate():
            email = form.email.data
            email += "@insa-lyon.fr" #No need for email, we ask the full email already
            person = Person.query.filter_by(email=email).first()
            if person is None:
                problem = u'L\'utilisateur %s n\'existe pas' %email
                flash(problem, u'error_forgetpassword')
            else:
                mdp = generate_mdp()
                problem = u'La demande de reinitialisation vous a été envoyée '
                person.password=hash_password(mdp)
                db.session.commit()
                mail_mot_de_passe_oublie(person.nickname, person.email, mdp)

                flash(problem, u'ok_forgetpassword')
            return render_template('auth/forgetpassword.html')
        else:
            problem = u'Problème dans le formulaire - Vous ne devez pas écrire @insa-lyon.fr'
            flash(problem, u'error_forgetpassword')
            return render_template('auth/forgetpassword.html')


# Deconnexion
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        if checkSession() is True:
            clearSession()
        return redirect(url_for('home'))

def date2Timestamp(hour, formatage="%d-%m-%Y"):
    """This function allows to convert a date into a timestamp"""
    return int(time.mktime(datetime.datetime.strptime(hour, formatage).timetuple()))

@app.route('/questionsante', methods=['POST'])
@login_required
def questionSante():
    if request.method == 'POST':
        numeroQuestion = request.form['input-numeroQuestion']
        value = request.form['input-value']
        person = getPersonFromSession()
        question = Questions.query.filter_by(person_id=person.id).first()
        if int(numeroQuestion) == 1:
            question.firstValue = value
            db.session.commit()
        elif int(numeroQuestion) == 2:
            question.secondValue = value
            db.session.commit()
        elif int(numeroQuestion) == 3:
            question.thirdValue = value
            db.session.commit()
        return jsonify(result="OK")

@login_required
def jourQuestionSante():
    dateToday = date.today().strftime('%d-%m-%Y')
    timestampToday = date2Timestamp(str(dateToday))

    dateDebutMouvinsa = datetime.datetime(2015, 03, 05).strftime('%d-%m-%Y')
    timestampDateDebutMouvinsa = date2Timestamp(str(dateDebutMouvinsa))

    # 02 avril
    dateMilieuMouvinsa = datetime.datetime(2015, 04, 02).strftime('%d-%m-%Y')
    timestampDateMilieuMouvinsa = date2Timestamp(str(dateMilieuMouvinsa))

    # 06 mai
    dateFinMouvinsa = datetime.datetime(2015, 05, 06).strftime('%d-%m-%Y')
    timestampdateFinMouvinsa = date2Timestamp(str(dateFinMouvinsa))

    person = getPersonFromSession()
    question = Questions.query.filter_by(person_id=person.id).first()

    if timestampToday >= timestampDateDebutMouvinsa and len(question.firstValue) == 0:
        return 1
    elif timestampToday >= timestampDateMilieuMouvinsa and len(question.secondValue) == 0:
        return 2
    elif timestampToday >= timestampdateFinMouvinsa and len(question.thirdValue) == 0:
        return 3
    else:
        return 0

#Page Personnelle
@app.route('/resultats/personnel', methods=['GET', 'POST'])
@login_required
def personnel():
    person = getPersonFromSession()

    if request.method == 'GET':

        todayDate = date.today()
        today = todayDate.strftime('%d-%m')

        startDate = datetime.datetime(2015, 02, 26)
        days = 70

        list_date_steps = {}

        for day in range(0, days):
            dateTemp = startDate + timedelta(days=day)

            stepsDay = Steps.query.filter_by(person_id=person.id, date=dateTemp).first()

            if stepsDay:
                list_date_steps[dateTemp] = stepsDay.stepnumber
            else:
                list_date_steps[dateTemp] = 0

        stepNumberPerson = round(FitnessInfo.query.filter_by(person_id=person.id).first().stepSum * 0.00064, 2)

        sortedDateSteps = sorted(list_date_steps.items(), key=operator.itemgetter(0))
        chartDates = ["["]
        chartValues = ["["]
        chartObjectifs = ["["]

        dateToday = datetime.datetime.today()

        goal = person.fitnessInfo.goal or "0"

        for dateIt in sortedDateSteps:
            if dateIt[0] > dateToday:
                break
            chartObjectifs.append(str(goal))
            chartObjectifs.append(',')
            chartDates.append("'" + dateIt[0].strftime('%d-%m') + "'")
            chartDates.append(',')
            chartValues.append(str(dateIt[1]))
            chartValues.append(',')

        chartValues.pop()
        chartDates.pop()
        chartObjectifs.pop()

        chartValues = (" ".join(chartValues) + "]")
        chartDates = (" ".join(chartDates) + "]")
        chartObjectifs = (" ".join(chartObjectifs) + "]")

        jQuesSante = 0 #jourQuestionSante()
        if jQuesSante != 0:
            display = "display:block;"
            title = u'Niveau d\'activité physique'
        else:
            display = ""
            title =""

        return render_template('person/main.html', title=title, display=display, jQuesSante=jQuesSante, chartValues=chartValues, chartDates=chartDates, chartObjectifs=chartObjectifs, person=person, today=today, list_date_steps=sortedDateSteps, stepNumberPerson=stepNumberPerson)
    elif request.method == 'POST':
        return UserController.validateStepsData(request, person)


#Page d'équipe
@app.route('/resultats/equipe', methods=['GET', 'POST'])
#@login_required
def group():
    person = getPersonFromSession()
    if person != "none" and 'idEquipe' not in request.args:
        return render_template('group/main.html', group=person.group, person=person)
    else:
        if 'idEquipe' in request.args:
            idEq = request.args.get('idEquipe', '')
            try:
                idEqInt = int(idEq)
                if idEqInt>0 and idEqInt<43:
                    group = Group.query.filter_by(id=idEq).first()
                    person = getPersonFromSession()
                    return render_template('group/main.html', group=group, person=person)
                else:
                    error = u'ERROR : le parametre idEquipe doit etre un entier compris entre 1 et 43'
                    return error
            except ValueError:
                error = u'ERROR : le parametre idEquipe doit etre un entier compris entre 1 et 43'
                return error
        else:
            error = u'ERROR : le parametre idEquipe est demandé'
            return error


#Page Reglages
@app.route('/reglages/', methods=['GET', 'POST'])
@login_required
def reglages():
    person = getPersonFromSession()
    if request.method == 'GET':
        return UserController.displaySettings(request, person)
    elif request.method == 'POST':
        return UserController.validateSetting(request, person)
#-------------------------End web pages


#@app.route('/', methods=['GET', 'POST'])
#@app.route('/inscription', methods=['GET', 'POST'])
'''def inscription():
    form = InscriptionForm(request.form)
    if request.method == 'POST'and form.validate():
        utilisateurEmail = Person.query.filter_by(email = form.email.data).first()
        utilisateur_pseudo = Person.query.filter_by(nickname = form.surnom.data).first()
        if utilisateurEmail is None and utilisateur_pseudo is None:

            if form.categorie.data == 'Etudiant':
                student = Student()
                createStudent(form, student)
                db.session.add(student)
                db.session.commit()
                flash(u'Merci pour votre inscription '+student.nickname+u'. Vous allez recevoir un mail de confirmation dans quelques instants!!!:)', 'ok')
                surnom = form.surnom.data
                email = form.email.data
                categorie = 'Etudiant'
                nom = form.nom.data
                prenom = form.prenom.data
                sexe = form.sexe.data
                dateNaissance = form.dateNaissance.data
                poids = form.poids.data
                taille = form.hauteur.data
                cycle = form.cycle.data
                annee = form.annee.data
                departement = form.departement.data
                filiere = form.filiere.data
                position = form.position.data
                affiliation = form.affiliation.data
                #inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                #inscription_alert(inscrits="NOT DEFINED", surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                sendInscriptionMailAndAlert(inscrits=Person.query.count(), surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                return  render_template('inscription/inscription.html', form=form)
            else:
                employee = Employee()
                createEmployee(form, employee)
                db.session.add(employee)
                db.session.commit()
                flash(u'Merci pour votre inscription '+employee.nickname+u'. Vous allez recevoir un mail de confirmation dans quelques instants!!!:)', 'ok')
                surnom = form.surnom.data
                email = form.email.data
                categorie = form.categorie.data
                nom = form.nom.data
                prenom = form.prenom.data
                sexe = form.sexe.data
                dateNaissance = form.dateNaissance.data
                poids = form.poids.data
                taille = form.hauteur.data
                departement = form.departement.data
                filiere = form.filiere.data
                position = form.position.data
                affiliation = form.affiliation.data
                #inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle='NONE', annee='NONE', departement=departement, filiere=filiere, position=position, affiliation=affiliation)
                sendInscriptionMailAndAlert(inscrits=Person.query.count(), surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle='NONE', annee='NONE', departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                return  render_template('inscription/inscription.html', form=form)
        elif utilisateurEmail is not None:
            flash(u'L\'email que vous voulez utiliser existe déjà. ', 'errorEmail')
        else:
            flash(u'Le pseudonyme que vous voulez utiliser existe déjà. Veuillez choisir un autre. ', 'errorPseudo')
    return render_template('inscription/inscription.html', form=form)'''

@app.route('/addPas/', methods=['GET'])
#@login_required
def addPas():
    nbPas = int(request.args.get('pas', ''))
    idPers = int(request.args.get('id', ''))
    day = int(request.args.get('jour', ''))
    month = int(request.args.get('mois', ''))

    fitnessInfo = FitnessInfo.query.filter_by(person_id=idPers).first()
    date = datetime.datetime(2015, month, day)

    steps = Steps()
    steps.person_id = idPers
    steps.date = date
    steps.stepnumber = nbPas

    db.session.add(steps)

    fitnessInfo.stepSum = fitnessInfo.stepSum + nbPas
    person = Person.query.filter_by(id=idPers).first()
    groupNb = person.group_id
    group = Group.query.filter_by(id=groupNb).first()
    group.stepSum = group.stepSum + nbPas

    db.session.commit()

    return "Added " + str(nbPas) + " steps to " + person.nickname