__author__ = 'vcaen'

from app import db
from models import User

db.create_all()


# insert
db.session.add(User("test","test"))

#commit
