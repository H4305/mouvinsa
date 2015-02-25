#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
#

__author__ = 'afaraut'

moyenneDistancePas = 0.00064

import os
from mouvinsa.utils.passHash import check_password, hash_password
from mouvinsa.user.BDDManager import loadPersonByMail
from mouvinsa.models import db, Steps, FitnessInfo, Group, Person, Level
from flask import jsonify
from datetime import date, timedelta
from werkzeug.utils import secure_filename, redirect
from mouvinsa.app import app
import datetime

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def loginmouv(email, password):
    person = loadPersonByMail(email)
    if person is None:
        return None, 1
    else:
        if check_password(person.password, password):
            return person, 0
        return None, 2

def change_password(person, password):
    person.password = hash_password(password)
    db.session.commit()
    return

def change_picture(person, file):
    if file and allowed_file(file.filename):
            # fileName, fileExtension = os.path.splitext('/path/to/somefile.ext')
            filename = secure_filename(str(person.id))
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            person.image = filename
            db.session.commit()
            return True
    return False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def change_info(person, birthdate, sex, weight, height, first):
    person.birthdate = birthdate
    person.sex = sex
    person.weight = weight
    person.height = height
    db.session.commit()
    return


def update_from_form(person, form):
    if form.password.data:
        form.password.data = hash_password(form.password.data)
    else:
        form.password.data = person.password

    if not form.image.data:
        form.image.data = person.image

    form.populate_obj(person)

    if form.goal.data:
        person.fitnessInfo.goal = int(form.goal.data)

    db.session.merge(person)
    db.session.commit()


def send_JSON_error(error_message):
    return jsonify(error=error_message)

def update_steps_ajax(person, form):
    step=form['input-step']
    cycle=form['input-cycle']
    swim=form['input-swim']
    daysToSubstract =form['date']

    if not step:
        step = 0

    if not cycle:
        cycle = 0

    if not swim:
        swim = 0

    try:
        stepsInt = int(step)
        cycleInt = int(cycle)
        swimInt = int(swim)
        daysToSubstractInt = int(daysToSubstract)

        if daysToSubstractInt<0 or daysToSubstractInt>2:
            error = "Date Invalide"
            return send_JSON_error(error_message=error)

        if stepsInt>=0 and cycleInt>=0 and swimInt>=0 and daysToSubstractInt>=0:

            #Formules conversion velo, swim
            stepsFromCycle = cycleInt * 150
            stepsFromSwimming = swimInt * 150
            newStepsTotal = stepsInt + stepsFromCycle + stepsFromSwimming
            # Steps day
            dateSteps = date.today() - timedelta(days=daysToSubstractInt)
            fitnessInfo = FitnessInfo.query.filter_by(person_id=person.id).first()
            stepsSumTotal = fitnessInfo.stepSum
            stepsForDay = Steps.query.filter_by(date=dateSteps, person_id=person.id).first()

            # List is not empty = that person has already entered steps once
            if stepsForDay:

                # I have to update with the new Number
                previousSteps = stepsForDay.stepnumber
                stepsToSum = previousSteps - newStepsTotal
                stepsForDay.stepnumber = newStepsTotal
                stepsSumTotal = stepsSumTotal - stepsToSum

            else:
            # List is empty -> New data
                steps = Steps()
                steps.person_id = person.id
                steps.date = dateSteps
                steps.stepnumber = newStepsTotal

                db.session.add(steps)
                stepsSumTotal = stepsSumTotal + newStepsTotal

            fitnessInfo.stepSum = stepsSumTotal
            personsTeam = Person.query.filter_by(group_id=person.group_id)
            teamSteps = 0

            for pers in personsTeam:
                teamSteps = teamSteps + FitnessInfo.query.filter_by(person_id=pers.id).first().stepSum

            group = Group.query.filter_by(id=person.group_id).first()
            group.stepSum = teamSteps
            distanceTot = "{0:.2f}".format(moyenneDistancePas * stepsSumTotal)
            city_changed = set_city_arrived_destination(moyenneDistancePas * stepsSumTotal, group)

            db.session.commit()
            update_streaks(dateSteps=dateSteps, person=person, fitnessInfo=fitnessInfo)
            db.session.commit()

            return jsonify(date=dateSteps.strftime('%d/%m/%Y'), stepj=newStepsTotal, distanceTot=distanceTot, cityChanged=city_changed, streak=fitnessInfo.streak, bestStreak=fitnessInfo.bestStreak)

        else:
            error = u'Une des valeurs rentrée est inférieure à 0.'
            return send_JSON_error(error_message=error)
    except ValueError:
        error = u'Une des valeurs rentrée n\'est pas numérique.'
        return send_JSON_error(error_message=error)


def set_city_arrived_destination(distanceGroup, group):

    city_changed = 'no'
    if distanceGroup < 200:
        group.city_arrived_id = 35
        group.city_destination_id = group.city_tres_facile_id
    elif distanceGroup >= 200 and distanceGroup < 450:
        group.city_arrived_id = group.city_tres_facile_id
        group.city_destination_id = group.city_facile_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom
    elif distanceGroup >= 450 and distanceGroup < 700:
        group.city_arrived_id = group.city_facile_id
        group.city_destination_id = group.city_moyen_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom
    elif distanceGroup >= 700 and distanceGroup < 1100:
        group.city_arrived_id = group.city_moyen_id
        group.city_destination_id = group.city_difficile_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom
    elif distanceGroup >= 1100 and distanceGroup < 1700:
        group.city_arrived_id = group.city_difficile_id
        group.city_destination_id = group.city_tres_difficile_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom
    elif distanceGroup >= 1700 and distanceGroup < 3000:
        group.city_arrived_id = group.city_tres_difficile_id
        group.city_destination_id = group.city_champion_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom
    elif distanceGroup >= 3000:
        group.city_arrived_id = group.city_champion_id
        group.city_destination_id = group.city_champion_id
        city_changed = u'Félicitations! Ton équipe vient d\'arriver à %s' %group.city_arrived.nom

    return city_changed

def checkStreakController(todayDate, person, fitnessInfo):
    yesterday = get_previous_date(todayDate)
    stepsYesterday = Steps.query.filter_by(date=yesterday, person_id=person.id).first()
    stepsToday = Steps.query.filter_by(date=todayDate, person_id=person.id).first()
    objPerso = fitnessInfo.goal

    if not stepsYesterday or stepsYesterday.stepnumber > objPerso and not stepsToday or stepsToday.stepnumber > objPerso:
        fitnessInfo.streak = 0

    db.session.commit()

    return

def update_streaks(dateSteps, person, fitnessInfo):

    newStreak = 0

    today = date.today()
    stepsDay = Steps.query.filter_by(person_id=person.id, date=today).first()
    yesterday = get_previous_date(today)
    stepsYesterday = Steps.query.filter_by(date=yesterday, person_id=person.id).first()

    startDate = datetime.date(2015, 02, 26)
    competitionDays = today - startDate

    objPerso = fitnessInfo.goal

    if dateSteps == today and stepsDay.stepnumber > objPerso:

        newStreak = 1

        for i in range(1,competitionDays.days + 1):
            dateTest = today - timedelta(days=i)
            stepsDay = Steps.query.filter_by(person_id=person.id, date=dateTest).first()

            if stepsDay and stepsDay.stepnumber > objPerso:
                newStreak = newStreak + 1
            else:
                break

        fitnessInfo.streak = newStreak

    #Not today. I check if today I put steps. Otherwise it will count only for the bestStreak
    else:

        if stepsDay and stepsDay.stepnumber > objPerso:
            newStreak = 1

            for i in range(1,competitionDays.days + 1):
                dateTest = today - timedelta(days=i)
                stepsDay = Steps.query.filter_by(person_id=person.id, date=dateTest).first()

                if stepsDay and stepsDay.stepnumber > objPerso:
                    newStreak = newStreak + 1
                else:
                    break

            fitnessInfo.streak = newStreak

        else:

            if stepsYesterday and stepsYesterday.stepnumber > objPerso:

                for i in range(0,competitionDays.days + 1):
                    dateTest = yesterday - timedelta(days=i)
                    stepsDay = Steps.query.filter_by(person_id=person.id, date=dateTest).first()

                    if stepsDay and stepsDay.stepnumber > objPerso:
                        newStreak = newStreak + 1
                    else:
                        break

            else:

                for i in range(0,competitionDays.days + 1):
                    dateTest = dateSteps - timedelta(days=i)
                    stepsDay = Steps.query.filter_by(person_id=person.id, date=dateTest).first()

                    if stepsDay and stepsDay.stepnumber > objPerso:
                        newStreak = newStreak + 1
                    else:
                        break

    if newStreak > fitnessInfo.bestStreak:
        fitnessInfo.bestStreak = newStreak


    if Steps.query.filter_by(person_id=person.id, date=today).first().stepnumber < objPerso:
        fitnessInfo.streak = 0

    return

def get_previous_date(date):
    return date - timedelta(days=1)
