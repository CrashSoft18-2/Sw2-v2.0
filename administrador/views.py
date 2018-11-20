from utils import *
from alumno.models import *
from profesor.models import *
from administrador.models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/administrador")
def inicioAdministrador():
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

@app.route("/administrador/displayProximasAsesorias")
def admDisplayAsesorias():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Administrador':
			profesores = Profesor.query.all()
			username = session['username']
			return render_template('administrador/displayProximasAsesorias.html', profesores = profesores, usuario = username)
		else:
			session['AUTH'] = None
			return redirect("/administrador")
	else:
		session['AUTH'] = None
		return redirect("/administrador")

@app.route("/administrador/displayAsesoriasDetalle/<int:id>")
def admDetalleProfesor(id):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Administrador':
			profesor = Profesor.query.filter_by(idProfesor=id).first()
			fecha = datetime.date.today()
			username = session['username']
			return render_template('administrador/detalleProfesor.html', profesor=profesor, fecha=fecha, usuario=username)
		else:
			session['AUTH'] = 'Vacio'
			return render_template('administrador/login.html')
	else:
		session['AUTH'] = 'Vacio'
		return redirect("/alumno")

@app.route("/administrador/programarAsesorias")
def programarAsesoriasAdm():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Administrador':
			username = session['username']
			return render_template('administrador/detalleProfesor.html', usuario=username)
		else:
			session['AUTH'] = 'Vacio'
			return render_template('administrador/login.html')
	else:
		session['AUTH'] = 'Vacio'
		return redirect("/alumno")

@app.route("/administrador/cerrarSesion")
def cerrarSesionAdm():
	session['AUTH'] = None
	session['id'] = None
	session['username'] = None
	session['nombre'] = None
	return redirect("/administrador")
