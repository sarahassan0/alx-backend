#!/usr/bin/env python3

"""
    Flask app entry point.
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


def get_locale() -> str:
    """
        Determine the best match of supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel: Babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
        App entry point
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
