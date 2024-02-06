#!/usr/bin/env python3

"""
    Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


class Config:
    """
        Bable configrations
    """
    LANGUAGES: List = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.locale_selector
def get_locale() -> str:
    """
        Determine the best match of supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
        App entry point
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
