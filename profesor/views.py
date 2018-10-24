from utils import *
from alumno.models import *
from profesor.models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/profesor")
def profesorInicio():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return loginProfesor()
		elif session['AUTH'] == 'Alumno':
			return redirect("/alumno"/)
		else:
			session['AUTH'] = 'Vacio'
			return render_template('alumno/login.html', val = False)
	else:
		session['AUTH'] = 'Vacio'
		return render_template('alumno/login.html', val = False)
	return render_template('profesor/login.html')

@app.route("/profesor/login", methods=['POST'])
def loginProfesor():
	return render_template('temp/temp.html')
