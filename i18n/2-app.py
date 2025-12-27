#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 2-index.html
    """
    return render_template('2-index.html')


def get_locale() -> str:
    """ Determines best match for supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Initialize Babel with the application
babel = Babel()
babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
