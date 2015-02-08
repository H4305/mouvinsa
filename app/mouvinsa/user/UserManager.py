__author__ = 'afaraut'

from mouvinsa.utils.passHash import check_password
from mouvinsa.user.BDDManager import loadPersonByMail

def loginmouv(email, password):
    person = loadPersonByMail(email)
    if person is None:
        return None, 1
    else:
        if check_password(person.password, password):
            return person, 0
        return None, 2
