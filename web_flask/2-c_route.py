#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function tat returns a message. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function tat returns a message. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Function tat returns a message. """
    text = text.replace("_", " ")
    return "C %s" % escape(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
