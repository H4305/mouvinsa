from sqlalchemy import Enum

from app import db


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
    weight = db.Column(db.Float,nullable=True)
    height = db.Column(db.Float, nullable=True)
    category = db.Column('category', Enum('etudiant', 'enseignant', 'iatos'), nullable=False)
    type = db.Column(db.String(50))
    etat = db.Column('etat', Enum('PREREGISTERED','REGISTERED', 'DROPPED'), nullable=False)
    token = db.Column(db.String(128), unique=True)

    def __init__(self):
        print "init person"

    def __repr__(self):
        return self.nickname

    __mapper_args__ = {
        'polymorphic_identity':'person',
        'polymorphic_on':type }


class Student(Person):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    year = db.Column(db.Integer)
    cycle = db.Column(db.Integer)
    branch = db.Column(db.Integer)

    __mapper_args__ =  {
        'polymorphic_identity':'student',
    }


class Employee(Person):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    affiliation = db.Column(db.String(255))
    position = db.Column(db.String(255))

    __mapper_args__ =  {
        'polymorphic_identity':'employee',
    }

