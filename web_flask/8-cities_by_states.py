#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    list_s = []
    list_c = []
    dico_s = storage.all(State)
    for k, v in dico_s.items():
        list_s.append(dico_s[k])
    list_so = sorted(list_s, key=lambda d: d.name)
    return render_template('8-cities_by_states.html',
                           list_s=list_so)


@app.teardown_appcontext
def tear_down(exception):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
