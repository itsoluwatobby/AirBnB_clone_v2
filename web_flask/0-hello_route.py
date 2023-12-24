#!/usr/bin/python3
"""
a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """A function that returns Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port='5000')
