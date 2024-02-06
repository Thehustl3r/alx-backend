#!/usr/bin/env python3
"""2-app"""
from flask import Flask, render_template, request
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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Determine the best match with our support language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
