from werkzeug.debug import DebuggedApplication
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from mouvinsa.config import SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
db = SQLAlchemy(app)


@app.before_first_request
def before_first_request():
    try:
        db.create_all()
    except Exception, e:
        app.logger.error(str(e))


app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

if app.debug:
    from werkzeug.debug import DebuggedApplication

    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.secret_key = 'ty6739hjDyaidjdjdd6tef908c'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
