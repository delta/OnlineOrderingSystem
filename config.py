import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'you-will-never-be-able-to-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_USE_SSL = True
MAIL_USERNAME = 'contact@example.com'
MAIL_PASSWORD = 'your-password'

