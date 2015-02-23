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

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
            set_city_arrived_destination(moyenneDistancePas * stepsSumTotal, group)

            db.session.commit()

            return jsonify(date=dateSteps.strftime('%d/%m/%Y'), stepj=newStepsTotal, distanceTot=distanceTot)

        else:
            error = u'Une des valeurs rentrée est inférieure à 0.'
            return send_JSON_error(error_message=error)
    except ValueError:
        error = u'Une des valeurs rentrée n\'est pas numérique.'
        return send_JSON_error(error_message=error)


def set_city_arrived_destination(distanceGroup, group):

    if distanceGroup < 200:
        group.city_arrived_id = 35
        group.city_destination_id = group.city_tres_facile_id
    elif distanceGroup >= 200 and distanceGroup < 450:
        group.city_arrived_id = group.city_tres_facile_id
        group.city_destination_id = group.city_facile_id
    elif distanceGroup >= 450 and distanceGroup < 700:
        group.city_arrived_id = group.city_facile_id
        group.city_destination_id = group.city_moyen_id
    elif distanceGroup >= 700 and distanceGroup < 1100:
        group.city_arrived_id = group.city_moyen_id
        group.city_destination_id = group.city_difficile_id
    elif distanceGroup >= 1100 and distanceGroup < 1700:
        group.city_arrived_id = group.city_difficile_id
        group.city_destination_id = group.city_tres_difficile_id
    elif distanceGroup >= 1700 and distanceGroup < 3000:
        group.city_arrived_id = group.city_tres_difficile_id
        group.city_destination_id = group.city_champion_id
    elif distanceGroup >= 3000:
        group.city_arrived_id = group.city_champion_id
        group.city_destination_id = group.city_champion_id

    return
