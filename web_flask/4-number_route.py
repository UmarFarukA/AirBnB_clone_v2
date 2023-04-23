#!/usr/bin/python3
"""A Scripts that start a Flask web app
Routes:
    /: returns hello hbnb
    /hbnb: returns hbnh
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return “Hello HBNB!”


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return “HBNB”


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display c followed by the value of text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Display Python followd by  value of text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def n(n):
    """Display value of n only if integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)