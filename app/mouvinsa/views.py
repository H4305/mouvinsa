from flask import render_template, request, flash, url_for, redirect

from app import app, db
from controllers.inscription_controller import InscriptionForm
from models import Student
from models import Person
from controllers.signin_controller import LoginForm


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

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
            token_param = request.args.get('token')
            user_found = Person.query.filter_by(token = token_param).first()
            confirm = request.args.get('msg')
            form = ConfirmationForm(request.form)
            if request.method == 'GET':
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
                        return render_template('inscription/confirmation.html', user=user_found, msg='inscrit')
            return redirect(url_for('home'))

@app.route('/forgetpassword/', methods=['GET', 'POST'])
def forgetpassword():
    if request.method == 'GET':
        return render_template('auth/forgetpassword.html')
    elif request.method == 'POST':
        email = request.POST.get('email') # Peut être passé par une classe form ? mais pour un attribut ?
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
def test_inscription() :
    student = Student()
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

@app.route('/test/confirmation')
def test_confirmation() :
    person = Person.query.filter_by(username='test4').first()
    if person is not None:
        db.session.delete(person)
        db.session.commit()
    student2 = Student()
    student2.username = 'test4'
    student2.password = 'password'
    student2.email = 'email4@email.com'
    student2.category = 'etudiant'
    student2.etat = 'preregistered'
    student2.token = 'a0114'
    db.session.add(student2)
    db.session.commit()
    string = ""
    for student in Person.query.all():
        string += student.__repr__()+student.token+student.etat
    return string