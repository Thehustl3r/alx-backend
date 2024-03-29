#!/usr/bin/env python3
"""1-app"""
from flask import Flask, render_template
from flask_babel import Babel
# Config = __import__('config').Config


app = Flask(__name__, template_folder='templates')


class Config:
    """this is the config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Basic Template for Babel Implementation"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
