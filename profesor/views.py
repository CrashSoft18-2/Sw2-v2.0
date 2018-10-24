from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/profesor")
def profesorInicio():
	return render_template('profesor/login.html')

@app.route("/profesor/login", methods=['POST'])
def loginProfesor():
	return render_template('temp/temp.html')
