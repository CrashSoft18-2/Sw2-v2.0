from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/profesor")
def inicio():
	return render_template('profesor/login.html', val=False)
