#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

__author__ = 'marcomontalto'

from mouvinsa.models import db, Level, Group, City, Person, FitnessInfo

nomsGroupes = [ u"Jumperzap", u"Highjumps", u"Batsqueak", u"Athletebrring", u"Sportouch", u"Catcherparp", u"Frisbeeplonk",
                u"Skateroar", u"Tiecheep", u"Tennisbuzz", u"Volleytweet", u"Gearmeow", u"Outslouch", u"Hockeytwang",
                u"Rowingthump", u"Uniformfizz", u"Walkgrowl", u"Hardballping", u"Freethrowrip", u"Golfingsmash", u"Championouch",
                u"Hockeyhoot", u"Lutzboink", u"Fitnesstweet", u"Bowlingbelch", u"Runningshush", u"Surferfizz", u"Batbeep",
                u"Biathlonboom", u"Battingbuzz", u"Cyclingcuckoo", u"Dartdingdong", u"Divedrip", u"Fitnessfizzle", u"Footballfizz",
                u"Boxingboom", u"Movementbuzz", u"Waterskiwoof", u"Canoeingcheep", u"Crazy Legs", u"Catchmurmer", u'Crazy Steps']

levels = [u'Très facile', u'Facile', u'Moyen', u'Difficile', u'Très difficile', u'Champion']
distances = [200, 450, 700, 1100, 1700, 3000]

cities_tr_facile = [u'Genève', u'Marseille', u'Zurich', u'Grenoble']
cities_facile = [u'Paris', u'Nice', u'Stuttgart', u'Bordeaux', u'Barcelone', u'Milan']
cities_moyen = [u'Rome', u'Prague', u'Amsterdam', u'Berlin', u'Bruxelles', u'Londres']
cities_difficile = [u'Dublin', u'Budapest', u'Alger', u'Tunis', u'Lisbonne', u'Vienne']
cities_tr_difficile = [u'Istanbul', u'Bucharest', u'Casablanca', u'Athènes', u'Stockholm', u'Oslo']
cities_champion = [u'Moscou', u'Dakar', u'Montréal', u'San Juan(Puerto Rico)', u'Reykjavik', u'Rio de Janeiro']

def create_groups():
    for name in nomsGroupes:
        group = Group()
        group.label = name
        db.session.add(group)

    db.session.commit()

def create_levels():
    index_distances = 0
    for label in levels:
        level = Level()
        level.label = label
        level.distance = distances[index_distances]
        index_distances = index_distances + 1
        db.session.add(level)

    db.session.commit()

def create_cities():
    level_city = 1
    for city_name in cities_tr_facile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.level_id = level_city
        db.session.add(city)

    level_city = level_city + 1
    for city_name in cities_facile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    level_city = level_city + 1
    for city_name in cities_moyen:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    level_city = level_city + 1
    for city_name in cities_difficile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    level_city = level_city + 1
    for city_name in cities_tr_difficile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)


    level_city = level_city + 1
    for city_name in cities_champion:
        city = City()
        city.nom = city_name
        city.description = ""
        city.description_image_1 = ""
        city.description_image_2 = ""
        city.description_image_3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    db.session.commit()


def default_image():
    person = Person.query.all()
    for per in person:
        per.image="/static/images/person/defaultm.png"

    woman = Person.query.filter_by(sex="Féminin").all()
    for wom in woman:
        wom.image="/static/images/person/defaultf.png"

    db.session.commit()

def init_image_levels_cities():
    default_image()
    create_levels()
    create_cities()

def create_fitnessInfo():
    person = Person.query.all()
    for per in person:
        fitnessInfo = FitnessInfo()
        fitnessInfo.person_id=per.id
        fitnessInfo.goal = 10000