#!/usr/bin/python3
"""import flask module
"""
from flask import Flask

app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function for the home page
    """
   return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
