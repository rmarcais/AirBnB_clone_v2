#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape, render_template

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


@app.route('/python/', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """ Function tat returns a message. """
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Function tat returns a message. """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function tat returns a message. """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
