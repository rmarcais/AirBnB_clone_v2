#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    list_s = []
    list_a = []
    dico = storage.all(State)
    for k, v in dico.items():
        list_s.append(dico[k])
    list_o = sorted(list_s, key=lambda d: d.name)
    dico_a = storage.all(Amenity)
    for k, v in dico_a.items():
        list_a.append(dico_a[k])
    list_ao = sorted(list_a, key=lambda d: d.name)
    return render_template('10-hbnb_filters.html', list_s=list_o,
                           list_a=list_ao)


@app.route('/states/<id>', strict_slashes=False)
def states_id_list(id):
    list_s = []
    list_c = []
    dico_s = storage.all(State)
    dico_c = storage.all(City)
    for k, v in dico_s.items():
        if (v.id == id):
            list_s.append(dico_s[k])
            break
    return render_template('9-states.html',
                           list_s=list_s, list_c=list_c)


@app.teardown_appcontext
def tear_down(exception):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
