__author__ = 'vcaen'

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://root:h4305@localhost/mouvinsa'
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# email server
#MAIL_SERVER = 'smtp.gmail.com'
#MAIL_PORT = 465
#MAIL_USE_TLS = False
#MAIL_USE_SSL = True
#MAIL_USERNAME = 'montaltomarco0@gmail.com'
#MAIL_PASSWORD = ''

# administrator list
#ADMINS = ['montaltomarco0@gmail.com']



# email server
MAIL_SERVER = 'smtp.insa-lyon.fr'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'marco.montalto@insa-lyon.fr'
MAIL_PASSWORD = ''

# administrator list
ADMIN = ['montaltomarco0@gmail.com']