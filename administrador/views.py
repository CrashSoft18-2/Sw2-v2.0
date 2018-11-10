from utils import *
from alumno.models import *
from profesor.models import *
from administrador.models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/administrador")
def inicioAdministrador():
	print(Administrador.query.all())
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador/displayProximasAsesorias')
		else:
			session['AUTH'] = None
			return render_template('administrador/login.html', val = False)
	else:
		session['AUTH'] = None
		return render_template('administrador/login.html', val = False)
	


@app.route("/administrador/login", methods=['POST'])
def loginAdministrador():
	pw = encode(request.form['uname'], request.form['psw'])
	administrador = Administrador.query.filter_by(usuarioAdministrador=request.form['uname'], contrasena=pw).first()
	if administrador:
		session['AUTH'] = 'Administrador'
		session['id'] = administrador.idAdministrador
		session['username'] = administrador.usuarioAdministrador
		return redirect("/administrador/displayProximasAsesorias")
	else:
		return render_template('administrador/login.html', val = True)
