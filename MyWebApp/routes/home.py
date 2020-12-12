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
    
def question_one():
    """
    returns first question
    """
    return render_template('first.html')
    
def question_two():
    """
    returns second question
    """
    return render_template('second.jinja2')
    

def contact():
    """
    returns contact information
    """
    return render_template('contact.jinja2')
