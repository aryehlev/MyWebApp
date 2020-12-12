"""
import from flask and models and db
"""
# pylint: disable=redefined-outer-name, no-member, consider-using-enumerate

from flask import render_template, request, session, jsonify
from models import Branch, BranchPrice, Product
from app import db, supermarket_info_dictionary as sd



def home():
    """
    returns landing page of application
    """
    return render_template('home.html')


