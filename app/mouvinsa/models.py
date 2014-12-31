#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8
from sqlalchemy import Enum

from mouvinsa.app import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    category = db.Column('category', Enum('etudiant', 'enseignant', 'iatos'), nullable=False)
    type = db.Column(db.String(50))

    def __init__(self):
        print "init person"

    def __repr__(self):
        return self.username

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type}


class Student(Person):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    year = db.Column(db.Integer)
    cycle = db.Column(db.Integer)
    branch = db.Column(db.Integer)

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
    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column('difficulty', Enum('difficile', 'moyen', 'facile'), nullable=False)
    label = db.Column(db.String(45), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(45), nullable=False)



