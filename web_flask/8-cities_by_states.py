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
    dico_c = storage.all(City)
    for k, v in dico_s.items():
        list_s.append(dico_s[k])
    list_so = sorted(list_s, key=lambda d: d.name)
    for k, v in dico_c.items():
        list_c.append(dico_c[k])
    list_co = sorted(list_c, key=lambda d: d.name)
    return render_template('8-cities_by_states.html',
                           list_s=list_so, list_c=list_co)


@app.teardown_appcontext
def tear_down(exception):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
