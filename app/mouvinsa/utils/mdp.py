__author__ = 'Anthony'

import os, random, string

def generate_mdp(length=13):
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for _ in range(length))