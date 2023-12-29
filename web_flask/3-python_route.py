#!/usr/bin/python3
"""import flask module
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function for the home page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the hbnb page
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """the c page
    """
    text = text.replace('_', ' ')
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """the python page
    """
    text = text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
