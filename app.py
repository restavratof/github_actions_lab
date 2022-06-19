""" Docstring """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def test():
    """Test method"""
    return "<p>FATA TEST</p>"
