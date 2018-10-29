from utils import *
from alumno.models_alumno import *
from profesor.models_profesor import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/administrador")
def administradorUC():
	return render_template('temp/temp.html')
