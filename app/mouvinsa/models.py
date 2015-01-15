from sqlalchemy import Enum
from sqlalchemy.orm import backref

from mouvinsa.app import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    # idGroup = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    category = db.Column('category', Enum('etudiant', 'enseignant', 'iatos'), nullable=False)
    type = db.Column(db.String(50))
    etat = db.Column('etat', Enum('PREREGISTERED', 'REGISTERED', 'DROPPED'), nullable=False)
    token = db.Column(db.String(128), unique=True)
    group_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self):
        print "init person"

    def __repr__(self):
        return self.nickname

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type}


class Student(Person):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    year = db.Column(db.String(120))
    cycle = db.Column(db.String(120))
    branch = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }


class Employee(Person):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    affiliation = db.Column(db.String(255))
    position = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
    }


class Goal(db.Model):
    __tablename__ = 'goal'
    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column('difficulty', Enum('difficile', 'moyen', 'facile'), nullable=False)
    label = db.Column(db.String(45), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(45), nullable=False)
    groups = db.relationship('Group', backref='goals', )


class Group(db.Model):
    __tablname__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(127), nullable=False)
    slogan = db.Column(db.String(255), nullable=True)
    stepSum = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255), nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.id'))
    persons = db.relationship('Person', backref='group',
                            lazy='dynamic')

class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    date = db.Column(db.DateTime)






