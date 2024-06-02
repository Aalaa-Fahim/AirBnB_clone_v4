#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from models import storage
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Close storage """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB route """
    cache_id = uuid.uuid4()
    return render_template('2-hbnb.html', cache_id=cache_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
