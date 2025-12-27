#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 4-index.html
    """
    return render_template('4-index.html')


def get_locale() -> str:
    """ Determines best match for supported languages """
    if request.args.get('locale'):
        requested_locale = request.args.get('locale')
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
