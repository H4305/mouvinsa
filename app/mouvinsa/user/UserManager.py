#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8
#
import os
from mouvinsa.utils.passHash import check_password, hash_password
from mouvinsa.user.BDDManager import loadPersonByMail
from mouvinsa.models import db, Steps
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
            #fileName, fileExtension = os.path.splitext('/path/to/somefile.ext')
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
        stepInt = int(step)
        cycleInt = int(cycle)
        swimInt = int(swim)
        daysToSubstractInt = int(daysToSubstract)

        if daysToSubstractInt<0 or daysToSubstractInt>2:
            error = "Date Invalide"
            return send_JSON_error(error_message=error)

        if stepInt>=0 and cycleInt>=0 and swimInt>=0 and daysToSubstractInt>=0:

            #Formules conversion velo, swim


            # Difference in days
            dateSteps = date.today() - timedelta(days=daysToSubstractInt)

            steps = Steps.query.filter_by(date=dateSteps, person_id=person.id).first()

            # List is not empty = that person has already entered steps once
            if steps:

                # I have to update with the new Number
                steps.stepnumber = steps.stepnumber + stepInt

            else:
            # List is empty -> New data
                steps = Steps()
                steps.person_id = person.id
                steps.date = dateSteps
                steps.stepnumber = stepInt

                db.session.add(steps)

            db.session.commit()

            return jsonify(date=dateSteps.strftime('%d/%m/%Y'), stepj=stepInt, stepSum=10)

        else:
            error = u'Une des valeurs rentrée est inférieure à 0.'
            return send_JSON_error(error_message=error)
    except ValueError:
        error = u'Une des valeurs rentrée n\'est pas numérique.'
        return send_JSON_error(error_message=error)