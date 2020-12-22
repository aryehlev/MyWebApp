"""
importing modules
"""
from os import environ
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.from_object('config.BaseConfig')
app.config['SECRET_KEY'] = 'dfsdg942352305jd'
app.config['TESTING'] = False
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')

# Database
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
db.init_app(app)
engine = create_engine('mysql+pymysql://Super_User:SuperX1234'
                       '@mysql-13101-0.cloudclusters.net:13101/SuperX',
                       echo=False)
session = Session(bind=engine)



# pylint: disable=wrong-import-position  disable=unused-import disable=wildcard-import disable=unused-wildcard-import
from routing import *


if __name__ == '__main__':
    app.run(debug=True)
