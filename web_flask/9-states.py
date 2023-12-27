#!/usr/bin/python3
"""
starts a Flask web application
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and
storage.all(...)
To load all cities of a State:
    * If your storage engine is DBStorage, you must use cities
    relationship
    * Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle @app.teardown_appcontext
    * Call in this method storage.close()
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
