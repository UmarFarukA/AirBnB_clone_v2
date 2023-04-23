#!/usr/bin/python3
"""A script that start python flask App"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=True)
def filters():
    """Display a html page for HBNB filters"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Function that close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
