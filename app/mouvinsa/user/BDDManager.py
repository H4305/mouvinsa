__author__ = 'Anthony'
from mouvinsa.models import Person

def loadPersonByMail(email):
    return Person.query.filter_by(email=email).first()

def loadPersonById(id):
    return Person.query.filter_by(id=id).first()