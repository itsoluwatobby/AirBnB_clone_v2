#!/usr/bin/python3
"""
a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
            sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders an HTML psage with a list of State"""
    states = sorted(list(storage.all("State").values()),
                    key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown(exception):
    """Closes the current sqlalchemy sesssion"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
