"""
imports of sql-alchemy and flask login modules
"""
from sqlalchemy import Integer, Column, Text, Boolean, BigInteger, DECIMAL, UniqueConstraint
from flask_login import LoginManager, UserMixin
from app import db
#pylint: disable=too-few-public-methods

class User(UserMixin, db.Model):
    """
    User model for user table in database
    """
    __tablename__ = 'user'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(15))
    email = Column(db.String(50), unique=True)
    password = Column(db.String(80))
    

