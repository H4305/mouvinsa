from sqlalchemy import Enum
from flask.ext.sqlalchemy import SQLAlchemy
from mouvinsa.app import app

db = SQLAlchemy(app)


# Defining Tables for n-n relationship
badges_person = db.Table('badges_person',
                         db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                         db.Column('badge_id', db.Integer, db.ForeignKey('badge.id'))
)

"""city_goal = db.Table('city_goal',
                     db.Column('city_id', db.Integer, db.ForeignKey('city.id')),
                     db.Column('goal_id', db.Integer, db.ForeignKey('goal.id'))
)"""

person_steps = db.Table('person_steps',
                        db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                        db.Column('step_id', db.Integer, db.ForeignKey('steps.id'))
)

group_goals = db.Table('group_goals',
                       db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
                       db.Column('city_tres_facile_id', db.Integer, db.ForeignKey('city.id')),
                       db.Column('city_facile_id', db.Integer, db.ForeignKey('city.id')),
                       db.Column('city_moyen_id', db.Integer, db.ForeignKey('city.id')),
                       db.Column('city_difficile_id', db.Integer, db.ForeignKey('city.id')),
                       db.Column('city_tres_difficile_id', db.Integer, db.ForeignKey('city.id')),
                       db.Column('city_champion_id', db.Integer, db.ForeignKey('city.id'))
)

# Defining models
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
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
    image = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    steps = db.relationship('Steps', backref='person', lazy='dynamic')
    fitnessInfo = db.relationship('FitnessInfo', backref='person', lazy='dynamic')
    badges = db.relationship('Badge',
                             secondary=badges_person,
                             backref=db.backref('person', lazy='dynamic'))

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


class Level(db.Model):
    __tablename__ = 'level'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(127), nullable=False)
    distance = db.Column(db.Integer, nullable=False, unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'level',
    }

    cities = db.relationship('City', backref='level', lazy='dynamic')


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(127), nullable=False)
    description = db.Column(db.Text)
    image_atteinte1 = db.Column(db.String(120), nullable=True)
    image_atteinte2 = db.Column(db.String(120), nullable=True)
    image_atteinte3 = db.Column(db.String(120), nullable=True)
    image_but = db.Column(db.String(120), nullable=True)
    # lattitude = db.Column(db.Float, nullable=False)
    #longitude = db.Column(db.Float, nullable=False)
    #caption = db.Column(db.String(255))
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))

    #groups = db.relationship('Group', backref='cities', lazy='dynamic')
    __mapper_args__ = {
        'polymorphic_identity': 'city',
    }


"""class Goal(db.Model):
    __tablename__ = 'goal'
    id = db.Column(db.Integer, primary_key=True)
    #difficulty = db.Column('difficulty', Enum('difficile', 'moyen', 'facile'), nullable=False)
    #label = db.Column(db.String(45), nullable=False)
    #distance = db.Column(db.Integer, nullable=False)
    #image = db.Column(db.String(45), nullable=False)
    #groups = db.relationship('Group', backref='goals', lazy='dynamic')"""


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(127), nullable=False)
    slogan = db.Column(db.String(255), nullable=True)
    stepSum = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255), nullable=True)
    city_arrived_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    city_destination_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'group',
    }

    persons = db.relationship('Person', backref='group', lazy='dynamic')

    city_arrived = db.relationship(City, foreign_keys=city_arrived_id, backref='cities_arrived')
    city_destination = db.relationship(City, foreign_keys=city_destination_id, backref='cities_destination')


class Steps(db.Model):
    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    date = db.Column(db.DateTime)
    stepnumber = db.Column(db.Integer, default=0)


class FitnessInfo(db.Model):
    __tablename__ = 'fitnessInfo'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    stepSum = db.Column(db.Integer, default=0, nullable=True)
    streak = db.Column(db.Integer, default=0)
    bestStreak = db.Column(db.Integer, default=0)
    goal = db.Column(db.Integer, default=0)


class Badge(db.Model):
    __tablename__ = 'badge'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(127), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)


"""class Vip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)"""
