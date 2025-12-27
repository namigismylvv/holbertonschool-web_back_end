#!/usr/bin/env python3
""" Module to start a Flask web application """
from flask import Flask, render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ route to display a message"""
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """ Select a language translation """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
