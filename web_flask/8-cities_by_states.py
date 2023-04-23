#!/usr/bin/python3
"""A scripts that start flask app
The app listen on 0.0.0.0 on port 5000
Routes:
    /cities_by_states: List all states & related cities
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Function that load all cities to state"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Function that remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
