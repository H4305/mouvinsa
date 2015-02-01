#!/usr/bin/python
#  -*- coding: utf-8 -*-
# coding: utf-8

from flask import render_template, request, flash, url_for, redirect

from app import app
from controllers.inscription_controller import InscriptionForm
from controllers.confirmation_controller import ConfirmationForm, updateProfil, uploadImage
from models import db, Student, Person, Employee
from emails import sendInscriptionMailAndAlert, inscription_notification, inscription_alert, sendRappelRendezVous
from controllers.signin_controller import LoginForm
from controllers.inscription_controller import createEmployee, createStudent
from controllers.tirageGroups_controller import tirageGroups
from sqlalchemy import func
from mouvinsa.utils.passHash import check_password

@app.route('/')
def home():
    name = request.args.get('name', '')
    return render_template('index.html', name=name)

#@app.route('/', methods=['GET', 'POST'])
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm(request.form)
    if request.method == 'POST'and form.validate():
        utilisateurEmail = Person.query.filter_by(email = form.email.data).first()
        utilisateur_pseudo = Person.query.filter_by(nickname = form.surnom.data).first()
        if utilisateurEmail is None and utilisateur_pseudo is None:


            if form.categorie.data == 'Etudiant':
                student = Student()
                createStudent(form, student)
                db.session.add(student)
                db.session.commit()
                flash(u'Merci pour votre inscription '+student.nickname+u'. Vous allez recevoir un mail de confirmation dans quelques instants!!!:)', 'ok')
                surnom = form.surnom.data
                email = form.email.data
                categorie = 'Etudiant'
                nom = form.nom.data
                prenom = form.prenom.data
                sexe = form.sexe.data
                dateNaissance = form.dateNaissance.data
                poids = form.poids.data
                taille = form.hauteur.data
                cycle = form.cycle.data
                annee = form.annee.data
                departement = form.departement.data
                filiere = form.filiere.data
                position = form.position.data
                affiliation = form.affiliation.data
                #inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                #inscription_alert(inscrits="NOT DEFINED", surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                sendInscriptionMailAndAlert(inscrits=Person.query.count(), surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                return  render_template('inscription/inscription.html', form=form)
            else:
                employee = Employee()
                createEmployee(form, employee)
                db.session.add(employee)
                db.session.commit()
                flash(u'Merci pour votre inscription '+employee.nickname+u'. Vous allez recevoir un mail de confirmation dans quelques instants!!!:)', 'ok')
                surnom = form.surnom.data
                email = form.email.data
                categorie = form.categorie.data
                nom = form.nom.data
                prenom = form.prenom.data
                sexe = form.sexe.data
                dateNaissance = form.dateNaissance.data
                poids = form.poids.data
                taille = form.hauteur.data
                departement = form.departement.data
                filiere = form.filiere.data
                position = form.position.data
                affiliation = form.affiliation.data
                #inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle='NONE', annee='NONE', departement=departement, filiere=filiere, position=position, affiliation=affiliation)
                sendInscriptionMailAndAlert(inscrits=Person.query.count(), surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle='NONE', annee='NONE', departement=departement, filiere=filiere, position=position, affiliation=affiliation )
                return  render_template('inscription/inscription.html', form=form)
        elif utilisateurEmail is not None:
            flash(u'L\'email que vous voulez utiliser existe déjà. ', 'errorEmail')
        else:
            flash(u'Le pseudonyme que vous voulez utiliser existe déjà. Veuillez choisir un autre. ', 'errorPseudo')
    return render_template('inscription/inscription.html', form=form)

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
            token_param = request.args.get('token')
            user_found = Person.query.filter_by(token = token_param).first()
            confirm = request.args.get('msg')
            form = ConfirmationForm(request.form)
            if request.method == "POST":
                #Enregistrer profils
                if request.form['hidden'] == 'Enregistrer':
                    if form.validate():
                        updateProfil(form, user_found)
                        db.session.commit()
                        flash(u'Votre profil est bien enregistré.', 'infos_enregistrees')
                        return render_template('inscription/confirmation.html', user=user_found, msg='confirme', form=form, form_active=1)
                    else:
                        return render_template('inscription/confirmation.html', user=user_found, msg='confirme', form=form, form_active=1)
                #Enregistrer image
                elif request.form['hidden'] == 'Envoyer':
                    img_file = request.files['image_upload']
                    uploadImage(img_file, user_found)
                    db.session.commit()
                    flash(u'Vous avez bien enregistré votre photo de profil.', 'image_uploaded')
                    return render_template('inscription/confirmation.html', user=user_found, msg='confirme', form=form, form_active=2)
            else:
                if user_found is not None:
                    if user_found.etat == 'PREREGISTERED':
                        if confirm == 'confirme':
                            user_found.etat='REGISTERED'
                            db.session.commit()
                            return render_template('inscription/confirmation.html', user=user_found, msg='confirme', form=form)
                        elif confirm == 'refuse':
                            user_found.etat='DROPPED'
                            db.session.commit()
                            return render_template('inscription/confirmation.html', user=user_found, msg='refuse')
                    elif user_found.etat == 'REGISTERED':
                        redirect(url_for('login'))
            return render_template('index.html')

@app.route('/forgetpassword/', methods=['GET', 'POST'])
def forgetpassword():
    if request.method == 'GET':
        return render_template('auth/forgetpassword.html')
    elif request.method == 'POST':
        email = request.POST.get('email') # Peut etre passe par une classe form ? mais pour un attribut ?
        person = Person.query.filter_by(email=email).first()
        if person is None:
            problem = "The user doesn't exist"
            page = "500.html"
        else:
            # Ici faudra envoyer le mail
            print "test"
        return render_template('auth/forgetpassword.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/signin.html')
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            nickname = form.username.data
            password = form.password.data
            person = Person.query.filter_by(nickname=nickname).first()
            if person is None:
                problem = "The user doesn't exist"
                flash(u'L\'utilisateur n\'existe pas.', 'errorEmail')
                page = "auth/signin.html"
            else:
                if check_password(person.password, password): #Surment un truc a faire car le mdp sera pas en clair
                    problem = "You were successfully logged in"
                    flash(u'Connexion ok', 'erreurMotDePasse')
                    page = "apropos.html"
                else:
                    problem = "Connection refused"
                    flash(u'Connexion refusé', 'erreurIdentifiants')
                    page = "auth/signin.html"
            return render_template(page, form=form)

#
# @app.route('/team/<teamname>/')
# def team_page(teamname) :
#     return render_template('team/team.html', teamname=teamname)
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', error=e)

@app.route('/test/inscription')
@app.route('/test/inscription/<user>')
def test_inscription(user="TestUser"):
    student = Student()
    student.username = user
    student.password = 'password'
    student.email = user +'@email.com'
    student.nickname = user
    student.category = 'etudiant'
    db.session.add(student)
    db.session.commit()

    return "Insere : " + student.__repr__()

@app.route('/test/listuser')
def list_users() :
    string = '<table>'
    string += '<tr><th>id</th><th>lastname</th><th>image</th><th>firstname</th><th>birthdate</th><th>etat</th><th>sex</th></tr>'
    for student in Person.query.all():
        string += '<tr><td>'+student.__repr__()+'</td><td>'+unicode(student.lastname)+'</td><td>'+unicode(student.image)+'</td><td>'+unicode(student.firstname)\
                  +'</td><td>'+unicode(student.birthdate)+'</td><td>'+unicode(student.etat)+'</td><td>'+unicode(student.sex)
    string += '</table>'
    return string

# @app.route('/test/confirmation')
# def test_confirmation() :
#     person = Person.query.filter_by(nickname='test4').first()
#     if person is not None:
#         db.session.delete(person)
#         db.session.commit()
#     student2 = Student()
#     student2.nickname = 'test4'
#     student2.firstname=''
#     student2.lastname=''
#     student2.password = 'password'
#     student2.email = 'email4@email.com'
#     student2.category = 'etudiant'
#     student2.etat = 'preregistered'
#     student2.sex = ''
#     student2.token = 'a0114'
#     db.session.add(student2)
#     db.session.commit()
#     string = '<table>'
#     string += '<tr><th>lastname</th><th>image</th><th>firstname</th><th>birthdate</th><th>etat</th><th>sex</th></tr>'
#     for student in Person.query.all():
#         string += '<tr><td>'+student.__repr__()+'</td><td>'+unicode(student.lastname)+'</td><td>'+unicode(student.image)+'</td><td>'+unicode(student.firstname)\
#                   +'</td><td>'+unicode(student.birthdate)+'</td><td>'+unicode(student.etat)+'</td><td>'+unicode(student.sex)
#     string += '</table>'
#     return string

@app.route('/sendMail/<surnom>')
def sendTo(surnom):
    email = 'marco.montalto@insa-lyon.fr'
    # ...
    categorie = "Etudiant"
    nom = "Montalto"
    prenom = "Marco"
    sexe = "Masculin"
    dateNaissance = "21/02/1993"
    poids = "70"
    taille = "170"
    cycle = u"Deuxième"
    annee = u"Quatrième"
    departement = "IF"
    filiere = "NONE"
    position = "NONE"
    affiliation = "NONE"
    #inscription_notification(surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
    return 'Sending test is deactivated'
    #render_template('testMail.html', email=email, surnom=surnom, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation)

@app.route('/sendMailAlert')
def sendMailAlert() :
    inscrits = "50"
    email = 'marco.montalto@insa-lyon.fr'
    surnom = "surnom"
    # ...
    categorie = "Etudiant"
    nom = "Montalto"
    prenom = "Marco"
    sexe = "Masculin"
    dateNaissance = "21/02/1993"
    poids = "70"
    taille = "170"
    cycle = u"Deuxième"
    annee = u"Quatrième"
    departement = "IF"
    filiere = "NONE"
    position = "NONE"
    affiliation = "NONE"
    inscription_alert(inscrits=inscrits, surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
    sendInscriptionMailAndAlert(inscrits=Person.query.count(), surnom=surnom, email=email, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation )
    return 'Alert mail was sent'
    #render_template('testMail.html', email=email, surnom=surnom, categorie=categorie, nom=nom, prenom=prenom, sexe=sexe, dateNaissance=dateNaissance, poids=poids, taille=taille, cycle=cycle, annee=annee, departement=departement, filiere=filiere, position=position, affiliation=affiliation)

@app.route('/sendMailRappelMardi')
def sendMailRetirePodometre():
    message = "";
    index = 0;
    for person in Person.query.all():
        index = index + 1;
        if index<206:
            surnom = person.nickname
            #email = person.email
            #message += surnom + " " + email + "<br>";
            # DO NOT UNCOMMENT IT sendRappelRendezVous(surnom=surnom, email=email)
    return message

@app.route('/countCategories')
def countCategories():
    message = "students : "
    students = Person.query.filter_by(category = 'etudiant').count()
    message += str(students) + "<br>"

    message += "students WOMAN : "
    stwoman = Person.query.filter_by(sex = 'Feinin').filter_by(category = 'etudiant').count();
    message += str(stwoman) + "<br>"

    message += "students MAN : "
    sthomme = Person.query.filter_by(sex = 'Masculin').filter_by(category = 'etudiant').count();
    message += str(sthomme) + "<br><br>"


    message += "iatos : "
    iatos = Person.query.filter_by(category = 'iatos').count()
    message += str(iatos) + "<br>"

    message += "iatos WOMAN : "
    iawoman = Person.query.filter_by(sex = 'Feminin').filter_by(category = 'iatos').count();
    message += str(iawoman) + "<br>"

    message += "iatos MAN : "
    iahomme = Person.query.filter_by(sex = 'Masculin').filter_by(category = 'iatos').count();
    message += str(iahomme) + "<br><br>"


    message += "teachers : "
    teachers = Person.query.filter_by(category = 'enseignant').count()
    message += str(teachers) + "<br>"

    message += "teachers WOMAN : "
    thwoman = Person.query.filter_by(sex = 'Feminin').filter_by(category = 'enseignant').count();
    message += str(thwoman) + "<br>"

    message += "teachers MAN : "
    thhomme = Person.query.filter_by(sex = 'Masculin').filter_by(category = 'enseignant').count();
    message += str(thhomme) + "<br><br>"

    message += "sex inconnu : "
    sxinconnu = Person.query.filter_by(sex = 'Inconnu').count();
    message += str(sxinconnu) + "<br><br>"
    return message


@app.route('/groupes')
def attributionGroupes():
    tirageGroups()
    i = 1;
    message =""
    while (i<42):
        message += "<b>"+"Groupe " +str(i)+ ": "+ "</b><br>"
        groupe = Person.query.filter_by(group_id = i).all()
        message += "<table> "
        for person in groupe:
            message += "<tr><td><i>"+person.email +"  "+"</i></td><td>"+ person.category+"  "+"</td><td>"+ person.sex + "</td></tr>"
        message += "<table><br><br> "
        i=i+1

    return message



