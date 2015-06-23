"""The Flask app, with initialization and view functions."""

import os
import logging
from logging.handlers import RotatingFileHandler
import datetime
from flask import Flask, render_template, request, url_for
from flask import abort, jsonify, redirect
from sqlalchemy.orm import sessionmaker
from flask.ext.login import LoginManager, current_user
from flask.ext.login import login_user, login_required, logout_user
from flask.ext.sqlalchemy import SQLAlchemy

import config
import filters
from forms import *
from models import *


# app setup
app = Flask(__name__)
app.config.from_object(config)
app.appname = 'flasky'


# database setup
db = SQLAlchemy(app)
db.Model = Base

engine = db.create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


#setup logging
app.logger.setLevel(logging.DEBUG)
# app.logger.setHandler(logging.StreamHandler())

handler = RotatingFileHandler(
    os.path.join('log/{0}.log'.format(app.appname)), 
    maxBytes=10000000, 
    backupCount=10
)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in.'


@login_manager.user_loader
def load_user(user_id):
    """Hook for Flask-Login to load a User instance from a user ID."""
    return db.session.query(User).get(user_id)


# Load custom Jinja filters from the `filters` module.
filters.init_app(app)


@app.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return render_template('error/not_found.html'), 404


@app.template_global()
def appname():
    return app.appname


@app.route('/')
def home():
    return render_template('public/index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('appointment_list'))
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        email = form.username.data.lower().strip()
        password = form.password.data.lower().strip()
        user, authenticated = \
            User.authenticate(db.session.query, email, password)
        if authenticated:
            login_user(user)
            return redirect(url_for('home'))
        else:
            error = 'Incorrect username or password. Try again.'
    return render_template('user/login.html', form=form, error=error)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))
