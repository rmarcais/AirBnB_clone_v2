#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Returns a template that lists all State present in DBStorage. """
    list_s = []
    dico = storage.all(State)
    for k, v in dico.items():
        list_s.append(dico[k])
    list_o = sorted(list_s, key=lambda d: d.name)
    return render_template('7-states_list.html', list_s=list_o)


@app.teardown_appcontext
def tear_down(exception):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
