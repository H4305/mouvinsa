__author__ = 'marcomontalto'

from mouvinsa.models import db, Level, Group, City

nomsGroupes = [ u"Jumperzap", u"Highjumps", u"Batsqueak", u"Athletebrring", u"Sportouch", u"Catcherparp", u"Frisbeeplonk",
                u"Skateroar", u"Tiecheep", u"Tennisbuzz", u"Volleytweet", u"Gearmeow", u"Outslouch", u"Hockeytwang",
                u"Rowingthump", u"Uniformfizz", u"Walkgrowl", u"Hardballping", u"Freethrowrip", u"Golfingsmash", u"Championouch",
                u"Hockeyhoot", u"Lutzboink", u"Fitnesstweet", u"Bowlingbelch", u"Runningshush", u"Surferfizz", u"Batbeep",
                u"Biathlonboom", u"Battingbuzz", u"Cyclingcuckoo", u"Dartdingdong", u"Divedrip", u"Fitnessfizzle", u"Footballfizz",
                u"Boxingboom", u"Movementbuzz", u"Waterskiwoof", u"Canoeingcheep", u"Crazy Legs", u"Catchmurmer"]

levels = [ u"Très facile", u"Facile", u"Moyen", u"Difficile", u"Très difficile", u"Champion"]
distances = []

cities_tr_facile = []
cities_facile = []
cities_moyen = []
cities_difficile = []
cities_tr_difficile = []
cities_champion = []

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
        level.label = label;
        level.distance = distances[index_distances]
        index_distances = index_distances + 1
        db.session.add(level)

    db.session.commit()

def create_cities():
    level_city = 0
    for city_name in cities_tr_facile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.image_atteinte1 = ""
        city.image_atteinte2 = ""
        city.image_atteinte3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    ++level_city
    for city_name in cities_facile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.image_atteinte1 = ""
        city.image_atteinte2 = ""
        city.image_atteinte3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    ++level_city
    for city_name in cities_moyen:
        city = City()
        city.nom = city_name
        city.description = ""
        city.image_atteinte1 = ""
        city.image_atteinte2 = ""
        city.image_atteinte3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    ++level_city
    for city_name in cities_difficile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.image_atteinte1 = ""
        city.image_atteinte2 = ""
        city.image_atteinte3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    ++level_city
    for city_name in cities_tr_difficile:
        city = City()
        city.nom = city_name
        city.description = ""
        city.image_atteinte1 = ""
        city.image_atteinte2 = ""
        city.image_atteinte3 = ""
        city.image_but = ""
        city.level_id = level_city
        db.session.add(city)

    db.session.commit()

