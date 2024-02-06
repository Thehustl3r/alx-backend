#!/usr/bin/env python3
"""0-app"""
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Basic Template for Babel Implementation"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
