from flask import Flask, render_template, request, flash, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'fqsfqsfqsfsqfqfdfdsdsfvsdvdfvdfvndfkzje,f"'

from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

#sub_controller INSCRIPTION import
from inscription_controller import InscriptionForm

@app.route('/')
def hello_world():
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
@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)