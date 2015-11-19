#!/bin/env python

from flask import Flask
from flask.ext.pagedown import PageDown
from flaskext.markdown import Markdown


kwikifapp = Flask(__name__)
kwikifapp.appname = 'Kwiki App'
kwikifapp.config.SECRET_KEY = 'enydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
kwikifapp.config.SESSION_PROTECTION = 'strong'

pagedown = PageDown(kwikifapp)
Markdown(kwikifapp)


@kwikifapp.template_global()
def appname():
    return kwikifapp.appname


@kwikifapp.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return 'No page here, dood. 404!', 404
