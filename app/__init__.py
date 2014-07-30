import os
from flask import Flask
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

#from routes import mail
#mail.init_app(app)

db = SQLAlchemy(app)
# import routes
from app import routes,models
