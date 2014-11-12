import os
basedir = os.path.abspath(os.path.dirname(__file__))

#if the below question doesn't get cleared up probably just switch to whats in the Flask example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #why didnt I have to make a session??
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-wont-guess'