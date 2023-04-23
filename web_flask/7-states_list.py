#!/usr/bin/python3
"""A scripts that start python flask App"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def state_list():
    """Display list of states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removing the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
