#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    list_s = []
    list_a = []
    list_p = []
    dico = storage.all(State)
    for k, v in dico.items():
        list_s.append(dico[k])
    list_o = sorted(list_s, key=lambda d: d.name)
    dico_a = storage.all(Amenity)
    for k, v in dico_a.items():
        list_a.append(dico_a[k])
    list_ao = sorted(list_a, key=lambda d: d.name)
    dico_p = storage.all(Place)
    for k, v in dico_p.items():
        list_p.append(dico_p[k])
    list_po = sorted(list_p, key=lambda d: d.name)
    return render_template('100-hbnb.html', list_s=list_o,
                           list_a=list_ao, list_p=list_po)


@app.teardown_appcontext
def tear_down(exception):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
