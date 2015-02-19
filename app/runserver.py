import sys

__author__ = 'vcaen'
from mouvinsa.app import app
#log = open("/vagrant/flask.log", "w")
#log.close()

if __name__=='__main__':
    port = 8080
    if sys.argv[1] == 'debug':
        port = 8081
    app.run(host='0.0.0.0',port=port,debug=True)
