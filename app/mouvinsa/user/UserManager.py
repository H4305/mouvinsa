__author__ = 'afaraut'

from mouvinsa.utils.passHash import check_password, hash_password
from mouvinsa.user.BDDManager import loadPersonByMail
from mouvinsa.models import db

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

def change_info(person, birthdate, sex, weight, height):
    person.birthdate = birthdate
    person.sex = sex
    person.weight = weight
    person.height = height
    db.session.commit()
    return