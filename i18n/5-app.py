#!/usr/bin/env python3
"""Flask app with internationalization support"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns a user dictionary or None if ID cannot be found
    or if login_as was not passed"""
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, KeyError):
            return None
    return None


@app.before_request
def before_request():
    """Sets the user as a global on flask.g.user"""
    g.user = get_user()


def get_locale():
    """Determine the best match for supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """Route for the home page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
