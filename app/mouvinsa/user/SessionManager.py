__author__ = 'afaraut'

from flask import session

def saveInSession(email, nickname, idgroup):
    session['email'] = email
    session['nickname'] = nickname
    session['idGroup'] = idgroup

def checkSession():
    if 'email' not in session and 'nickname' not in session and 'idGroup' not in session:
        return False
    else:
        return True