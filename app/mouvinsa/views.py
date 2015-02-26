#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8


#-------------------Imports
from flask import render_template, request, flash, url_for, redirect
from app import app
from controllers.signin_controller import LoginForm, MdpForm
from models import db, Person, Group, Steps, FitnessInfo
from emails import mail_mot_de_passe_oublie
from mouvinsa.user import UserController
from mouvinsa.utils.passHash import hash_password
from mouvinsa.user.UserManager import loginmouv
from mouvinsa.user.SessionManager import saveInSession, checkSession, clearSession, getPersonFromSession, login_required
from mouvinsa.utils.mdp import generate_mdp
from datetime import date, timedelta
import datetime
import operator
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
    groups = Group.query.all()
    nbPasTotales = 0
    distanceTotale = 0
    for group in groups:
        nbPasTotales = nbPasTotales + group.stepSum
        distanceTotale = distanceTotale + group.distance
        toursTerre = round(distanceTotale/40075,2)
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


        return render_template('person/main.html', chartValues=chartValues, chartDates=chartDates, chartObjectifs=chartObjectifs, person=person, today=today, list_date_steps=sortedDateSteps, stepNumberPerson=stepNumberPerson)
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
