from functools import update_wrapper, wraps
from datetime import datetime
from flask import make_response

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

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)
