__author__ = 'marcomontalto'

from threading import Thread

from app import app

def async(f):
    def wrapper(*args, **kwargs):
        def inner(*args, **kwargs):
            with app.app_context():
                f(*args, **kwargs)
        t = Thread(target = inner, args = args, kwargs = kwargs)
        t.start()
    return wrapper
