#!/usr/bin/python3
"""
a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
            variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the
            text variable (replace underscore _ symbols with a space )
            * The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """A function that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    A function that returns the text content in the url
    Arguments:
        text<str> - a string retrieved from the last entry
                    in the url after '/c/'
    """
    text_params = text.replace('_', ' ')
    return "C {}".format(text_params)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def _python(text='is cool'):
    """
    A function that returns the text content in the url
    Arguments:
        text<str> - a string retrieved from the last entry
                    in the url after '/python/'
                    DEFAULT VALUE: text = 'is cool'
    """
    text_params = text.replace('_', ' ')
    return "Python {}".format(text_params)


@app.route('/number/<n>', strict_slashes=False)
def _number(n):
    """
    A function that returns the number content in the url
    Warning: Only integers allowed
    Arguments:
        n<int> - a string retrieved from the last entry
                    in the url after '/number/'
    """
    try:
        value = int(n)
        return "{} is a number".format(value)
    except Exception as e:
        return abort(404)


if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port='5000')
