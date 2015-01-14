__author__ = 'vcaen'
from mouvinsa.app import app
log = open("/vagrant/flask.log", "w")
log.close()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
