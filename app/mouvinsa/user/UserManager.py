__author__ = 'afaraut'

from mouvinsa.utils.passHash import check_password
from mouvinsa.models import Person

def loginmouv(email, password):
    person = Person.query.filter_by(email=email).first()
    if person is None:
        return None, 1
    else:
        if check_password(person.password, password):
            return person, 0
        return None, 2
