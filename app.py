from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

from app import profesor.views, alumno.views

import config

def init():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
	init()
