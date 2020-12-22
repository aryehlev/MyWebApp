"""
import from flask and models and db
"""
# pylint: disable=redefined-outer-name, no-member, consider-using-enumerate

from flask import render_template, request, session, jsonify

from app import db



def home():
    """
    returns landing page of application
    """
    return render_template('home.jinja2')
    
def projects():
    """
    returns project page
    """
    return "here ther will be projects"

def burgers():
    """
    returns burgers page
    """
    return "here ther will be burgers"

def contact():
    """
    returns contact information
    """
    return render_template('contact.jinja2')
