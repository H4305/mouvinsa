__author__ = 'vcaen'

from mouvinsa.app import db
from mouvinsa.models import User

db.create_all()


# insert
db.session.add(User("test","test"))

#commit
