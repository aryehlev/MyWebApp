"""
import app and routing modules
"""

from app import app
from routes import home, signup
from flask import session, request, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    main page route
    """
    return home.home()



@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    logging in route
    """
    return signup.login()


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    registering route
    """
    return signup.register()


@app.route('/cart', methods=['GET', 'POST'])


@app.route("/logout")
def logout():
    """
    logout route
    """
    return signup.logout()



@app.errorhandler(404)
def page_not_found():
    """
    route for 404 error handler
    """
    return render_template('404.html', title='404'), 404
