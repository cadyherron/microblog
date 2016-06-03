import os
basedir = os.path.abspath(os.path.dirname(__file__))

##########################
# SQLALCHEMY
##########################

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# SQLALCHEMY_TRACK_MODIFICATIONS = False


##########################
# FORMS
##########################

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


##########################
# OPENID
##########################

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


##########################
# SEND ERRORS VIA EMAIL
##########################

MAIL_SERVER = 'localhost'
MAIL_PORT = 2500
MAIL_USERNAME = None
MAIL_PASSWORD = None
ADMINS = ['you@example.com']


##########################
# PAGINATION
##########################
POSTS_PER_PAGE = 3


##########################
# WHOOSH FOR SEARCH
##########################
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
