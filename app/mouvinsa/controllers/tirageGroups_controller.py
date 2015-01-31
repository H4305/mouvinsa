__author__ = 'Liuda'
from mouvinsa.models import db, Student, Person, Employee

def tirageGroups():
    index = 0
    people = Person.query.filter().limit(3)
    etudiants = Person.query.filter_by(category='etudiant').all()
    enseignants = Person.query.filter_by(category='enseignant').all()
    iatos = Person.query.filter_by(category='iatos').all()
    
    for person in etudiants:
        index = index + 1
        person.group_id = index
        if index == 41:
            index=0

    index=0

    for person in enseignants:
        index = index + 1
        person.group_id = index
        if index == 41:
            index=11

    index=0

    for person in iatos:
        index = index + 1
        person.group_id = index
        if index == 41:
            index=34