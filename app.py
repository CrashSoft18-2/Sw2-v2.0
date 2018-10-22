from flask import Flask
import os

app = Flask(__name__)

from profesor.views import *

import config

def init():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
	init()
