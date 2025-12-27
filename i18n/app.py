#!/usr/bin/env python3
""" Route module for the API - Infer appropriate time zone"""

from os import getenv
from typing import Union, Optional
from datetime import datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from flask import Flask, request, render_template, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)


class Config(object):
    """ Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Dil ve zaman dilimi seçici fonksiyonlar


def get_locale() -> Optional[str]:
    """ Determines best match for supported languages """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user and g.user.get('locale') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> Optional[str]:
    """ Determines the timezone """
    if request.args.get('timezone'):
        tz_param = request.args.get('timezone')
        try:
            return timezone(tz_param).zone
        except UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except UnknownTimeZoneError:
            return None
    return app.config['BABEL_DEFAULT_TIMEZONE']


# Babel nesnesini oluştururken selector fonksiyonlarını bağla
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    return None


@app.before_request
def before_request() -> None:
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 6-index.html
    """
    tz = get_timezone()
    user_timezone = timezone(tz) if tz else timezone(
        app.config['BABEL_DEFAULT_TIMEZONE'])

    current_time = datetime.now(user_timezone)
    locale = get_locale()
    if locale == 'fr':
        formatted_time = current_time.strftime("%d %B %Y à %H:%M:%S")
    else:
        formatted_time = current_time.strftime("%b %d, %Y, %I:%M:%S %p")

    return render_template('6-index.html', current_time=formatted_time)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
