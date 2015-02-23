__author__ = 'vcaen'

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
HOME_DIR = os.path.expanduser('~')

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://root:h4305@localhost/mouvinsa'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# administrator list
ADMIN = ['mouvinsa.communication@gmail.com']

DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'mouvinsa.communication@gmail.com'
MAIL_PASSWORD = '**********'

DATE_DEBUT = "26/02/2015"
UPLOAD_FOLDER = HOME_DIR + '/mouvinsa/uploads'
UPLOAD_MAX_SIZE = 16 * 1024 * 1024
