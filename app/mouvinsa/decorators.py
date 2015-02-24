from functools import update_wrapper
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

def nocache(f):
    def new_func(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        resp.cache_control.no_cache = True
        return resp
    return update_wrapper(new_func, f)
