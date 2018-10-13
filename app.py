from flask import Flask
import os

app = Flask(__name__)

import config
import views

