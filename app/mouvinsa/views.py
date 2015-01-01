#!/usr/bin/python
#  -*- coding: utf-8 -*-

from flask import render_template, request, flash, url_for, redirect

from app import app, db
from controllers.inscription_controller import InscriptionForm
from controllers.confirmation_controller import ConfirmationForm
from models import Student, Person, Employee
from controllers.signin_controller import LoginForm
from controllers.inscription_controller import createEmployee, createStudent


@app.route('/')
def home():
    name = request.args.get('name', '')
    return render_template('index.html', name=name)


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():

    form = InscriptionForm(request.form)
    if request.method == 'POST': #and form.validate():

        if form.categorie.data == 'Etudiant':
            student = Student()
            createStudent(form, student)
            db.session.add(student)
            db.session.commit()
            return  "Merci pour votre inscription "+student.nickname + ". Vous allez recevoir un e-mail de confirmation contenant votre surnom et votre mot de passe !"
        else:
            employee = Employee()
            createEmployee(form, employee)
            db.session.add(employee)
            db.session.commit()

        return "Merci pour votre inscription, "+employee.nickname+". Vous allez recevoir un e-mail de confirmation contenant votre surnom et votre mot de passe !"
    else:
        return render_template('inscription/inscription.html', form=form)

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
            token_param = request.args.get('token')
            user_found = Person.query.filter_by(token = token_param).first()
            confirm = request.args.get('msg')
            form = ConfirmationForm(request.form)
            if request.method == "POST":
                if form.image.data is None:
                    user_found.lastname = form.lastname.data
                    user_found.firstname = form.firstname.data
                    user_found.weight = form.weight.data
                    user_found.height = form.height.data
                    user_found.birthdate = form.birthdate.data
                    db.session.commit()
                    flash('Vous avez bien enregistre votre profil! Maintenant vous pouvez vous connecter avec votre surnom et votre mot de passe.')
                    return redirect(url_for('login'))
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
                    #elif user_found.etat == 'REGISTERED':
                        #return render_template('inscription/confirmation.html', user=user_found, msg='inscrit')
                return redirect(url_for('home'))

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
            username = form.username.data
            password = form.password.data
            person = Person.query.filter_by(username=username).first()
            if person is None:
                problem = "The user doesn't exist"
                page = "500.html"
            else:
                if person.password == password: #Surment un truc a faire car le mdp sera pas en clair
                    problem = "You were successfully logged in"
                    page = "testeuh.html"
                    # Il faudra mettre vers Index
                else:
                    problem = "Connection refused"
                    page = "500.html"
            flash(problem)
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
    string = "List user <br/>"
    for student in Person.query.all():
        string += student.__repr__()+unicode(student.lastname)+unicode(student.firstname)\
                  +unicode(student.birthdate)+student.etat
    return string

@app.route('/test/confirmation')
def test_confirmation() :
    person = Person.query.filter_by(nickname='test4').first()
    if person is not None:
        db.session.delete(person)
        db.session.commit()
    student2 = Student()
    student2.nickname = 'test4'
    student2.password = 'password'
    student2.email = 'email4@email.com'
    student2.category = 'etudiant'
    student2.etat = 'preregistered'
    student2.sex = 'Masculin'
    student2.token = 'a0114'
    db.session.add(student2)
    db.session.commit()
    string = ""
    for student in Person.query.all():
        string += student.__repr__()+student.token+student.etat
    return string