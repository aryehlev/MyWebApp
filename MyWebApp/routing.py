"""
import app and routing modules
"""

from app import app
from routes import home
from flask import session, request, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    main page route
    """
    return home.home()

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    contact info route
    """
    return home.contact()


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    """
    projects route
    """
    return home.projects()

@app.route('/burgers', methods=['GET', 'POST'])
def burgers():
    """
    burgers route
    """
    return home.burgers()

@app.errorhandler(404)
def page_not_found():
    """
    route for 404 error handler
    """
    return render_template('404.html', title='404'), 404
