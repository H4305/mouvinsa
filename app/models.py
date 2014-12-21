from sqlalchemy import Enum

__author__ = 'vcaen'

from app import db



class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    nickname = db.Column(db.String(120), unique=True)
    sex = db.Column(db.String(1))
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    birthdate = db.Column(db.DateTime)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    category = db.Column('category', Enum('etudiant', 'enseignant', 'iatos'))

    def __init__(self, id, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "{}"

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    cycle = db.Column(db.Integer)
    branch = db.Column(db.Integer)
