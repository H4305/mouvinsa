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
            index=18

nomsGroupes = [ u"Jumperzap", u"Highjumps", u"Batsqueak", u"Athletebrring", u"Sportouch", u"Catcherparp", u"Frisbeeplonk",
                u"Skateroar", u"Tiecheep", u"Tennisbuzz", u"Volleytweet", u"Gearmeow", u"Outslouch", u"Hockeytwang",
                u"Rowingthump", u"Uniformfizz", u"Walkgrowl", u"Hardballping", u"Freethrowrip", u"Golfingsmash", u"Championouch",
                u"Hockeyhoot", u"Lutzboink", u"Fitnesstweet", u"Bowlingbelch", u"Runningshush", u"Surferfizz", u"Batbeep",
                u"Biathlonboom", u"Battingbuzz", u"Cyclingcuckoo", u"Dartdingdong", u"Divedrip", u"Fitnessfizzle", u"Footballfizz",
                u"Boxingboom", u"Movementbuzz", u"Waterskiwoof", u"Canoeingcheep", u"Crazy Legs", u"Catchmurmer"]
