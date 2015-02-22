#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
#

__author__ = 'afaraut'

moyenneDistancePas = 0.00064

from mouvinsa.utils.passHash import check_password, hash_password
from mouvinsa.user.BDDManager import loadPersonByMail
from mouvinsa.models import db, Steps, FitnessInfo, Group, Person
from flask import jsonify
from datetime import date, timedelta

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

def change_picture(person, image):
    return

def change_info(person, birthdate, sex, weight, height, first):
    person.birthdate = birthdate
    person.sex = sex
    person.weight = weight
    person.height = height
    db.session.commit()
    return

def update_from_form(person, form):
    form.password.data = hash_password(form.password.data)
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

            Group.query.filter_by(id=person.group_id).first().stepSum = teamSteps

            db.session.commit()

            distanceTot = "{0:.2f}".format(moyenneDistancePas * stepsSumTotal)

            return jsonify(date=dateSteps.strftime('%d/%m/%Y'), stepj=newStepsTotal, distanceTot=distanceTot)

        else:
            error = u'Une des valeurs rentrée est inférieure à 0.'
            return send_JSON_error(error_message=error)
    except ValueError:
        error = u'Une des valeurs rentrée n\'est pas numérique.'
        return send_JSON_error(error_message=error)