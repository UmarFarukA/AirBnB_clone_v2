#!/usr/bin/python3
"""A script that start python flask App"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Function that display all states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Function that get states by id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Function that close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
