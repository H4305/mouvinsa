__author__ = 'afaraut'

from functools import wraps
from flask import session, request, redirect, url_for
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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function