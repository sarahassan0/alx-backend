#!/usr/bin/env python3

"""
    Flask app entry point.
"""

from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    "app Enty point"
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
