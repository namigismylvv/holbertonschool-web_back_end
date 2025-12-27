#!/usr/bin/env python3
"""
Module to start a Flask web application with internationalization support.

This module demonstrates setting up a basic Flask application with support for
internationalization, including language selection based on user preference or
browser settings.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for setting Flask and Babel configurations."""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for the user's locale.

    Returns:
        A string representing the best match for the user's preferred language.
    """
    user_locale = request.args.get('locale')
    if user_locale and user_locale in Config.LANGUAGES:
        return user_locale

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> dict:
    """
    Retrieve a user from the request query parameters.

    Attempts to find a user by the 'login_as' query parameter and returns the
    user information if found.

    Returns:
    A dictionary containing user information or None if no valid user is found.
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Hook to run before each request to set the global user.

    Retrieves a user based on the request parameters and sets it globally
    for the current request context.
    """
    g.user = get_user()


@app.route('/', methods=["GET"])
def index() -> str:
    """
    Render the initial template with a greeting.

    Returns:
        Rendered template for the index page.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
