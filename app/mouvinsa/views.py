from flask import render_template, request, flash, url_for, redirect

from mouvinsa.app import app, db
from mouvinsa.controllers.inscription_controller import InscriptionForm
from models import Student
from mouvinsa.models import Person


@app.route('/')
def home():
    name = request.args.get('name', '')
    return render_template('index.html', name=name)

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():

    form = InscriptionForm(request.form)
    if request.method == 'POST':
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('inscription/inscription.html', form=form)

@app.route('/login/', methods=['GET', 'POST'] )
def login():
    return render_template('auth/signin.html')
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
def test_inscription() :
    student = Student()
    student.username = 'test'
    student.password = 'password'
    student.email = 'email@email.com'
    student.nickname = 'test'
    student.category = 'etudiant'
    db.session.add(student)
    db.session.commit()


    return student.__repr__()

@app.route('/test/listuser')
def list_users() :
    string = ""
    for student in Person.query.all():
        string += student.__repr__()

    return string