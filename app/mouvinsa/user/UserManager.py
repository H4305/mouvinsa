__author__ = 'afaraut'

from mouvinsa.utils.passHash import check_password, hash_password
from mouvinsa.user.BDDManager import loadPersonByMail
from mouvinsa.models import db
from flask import jsonify

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
    date=form['date']

    if date != 0 or date != 1 or date != 2:
        error = "Date Invalide"
        return send_JSON_error(error_message=error)
    try:
        stepInt = int(step)
        cycleInt = int(cycle)
        swimInt = int(swim)
        dateInt = int(date)
        if stepInt>=0 and cycleInt>=0 and swimInt>=0 and dateInt>=0:

            #Formules conversion velo, swim



            db.session.commit()

            return jsonify(date=date, stepj=stepInt, stepSum=10)

        else:
            error = "Une des valeurs rentrée est inférieure à 0."
            return send_JSON_error(error_message=error)
    except ValueError:
        error = "Une des valeurs rentrée n'est pas numérique."
        return send_JSON_error(error_message=error)