__author__ = 'Liuda'
from mouvinsa.models import db, Student, Person, Employee, Group
nomsGroupes = [ u"Jumperzap", u"Highjumps", u"Batsqueak", u"Athletebrring", u"Sportouch", u"Catcherparp", u"Frisbeeplonk",
                u"Skateroar", u"Tiecheep", u"Tennisbuzz", u"Volleytweet", u"Gearmeow", u"Outslouch", u"Hockeytwang",
                u"Rowingthump", u"Uniformfizz", u"Walkgrowl", u"Hardballping", u"Freethrowrip", u"Golfingsmash", u"Championouch",
                u"Hockeyhoot", u"Lutzboink", u"Fitnesstweet", u"Bowlingbelch", u"Runningshush", u"Surferfizz", u"Batbeep",
                u"Biathlonboom", u"Battingbuzz", u"Cyclingcuckoo", u"Dartdingdong", u"Divedrip", u"Fitnessfizzle", u"Footballfizz",
                u"Boxingboom", u"Movementbuzz", u"Waterskiwoof", u"Canoeingcheep", u"Crazy Legs", u"Catchmurmer"]

def create_groups():
    for name in nomsGroupes:
        group = Group()
        group.label = name
        db.session.add(group)

    db.session.commit()

def tirageGroups():

    index = 0
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

    #lara.chevallier
    pers = Person.query.filter_by(id=98).first()
    pers.group_id = 39
    #emilie.cloue
    pers = Person.query.filter_by(id=109).first()
    pers.group_id = 39
    #guillaume.marie
    pers = Person.query.filter_by(id=101).first()
    pers.group_id = 37
    #raynold.richard
    pers = Person.query.filter_by(id=118).first()
    pers.group_id = 37

    #laurentiu.capatina
    pers = Person.query.filter_by(id=34).first()
    pers.group_id = 22
    #olivier.merchiers
    pers = Person.query.filter_by(id=67).first()
    pers.group_id = 22
    #maria.baboulall
    pers = Person.query.filter_by(id=80).first()
    pers.group_id = 9
    #chantal.berdier
    pers = Person.query.filter_by(id=117).first()
    pers.group_id = 9

    db.session.commit()
