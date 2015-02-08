__author__ = 'afaraut'

from flask import session
from mouvinsa.user.BDDManager import loadPersonById

def saveInSession(id):
    session['id'] = id

def checkSession():
    if 'id' not in session:
        return False
    else:
        return True

def clearSession():
    session.clear()

def getPersonFromSession():
    return loadPersonById(session['id'])