from utils import *
from alumno.models import *
from profesor.models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/profesor")
def inicioProfesor():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return loginProfesor()
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = 'Vacio'
			return render_template('profesor/login.html', val = False)
	else:
		session['AUTH'] = 'Vacio'
		return render_template('profesor/login.html', val = False)
	


@app.route("/profesor/login", methods=['POST'])
def loginProfesor():
	pw = encode(request.form['uname'], request.form['psw'])
	profesores = Profesor.query.all()
	for p in profesores:
		p.contrasena = encode(p.usuarioProfesor, request.form['psw'])
	alumnos = Alumno.query.all()
	for a in alumnos:
		a.contrasena = encode(a.usuarioAlumno, request.form['psw'])
		
	db.session.commit()
	
	profesor = Profesor.query.filter_by(usuarioProfesor=request.form['uname'], contrasena=pw).first()
	if profesor:
		session['AUTH'] = 'Profesor'
		session['id'] = profesor.idProfesor
		session['username'] = profesor.usuarioProfesor
		session['nombre'] = profesor.nombre
		return redirect("/profesor/displayProximasAsesorias")
	else:
		return render_template('profesor/login.html', val = True)

	
@app.route("/profesor/displayProximasAsesorias")
def indexProfesor():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			profesor = Profesor.query.filter_by(usuarioProfesor=session['username']).first()
			username = session['username']
			fecha = datetime.date.today()
			return render_template('profesor/proximasAsesorias.html', profesor = profesor, usuario = username, fecha = fecha)
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = 'Vacio'
			return redirect("/profesor")
	else:
		session['AUTH'] = 'Vacio'
		return redirect("/profesor")
	

@app.route("/profesor/cerrarSesion")
def cerrarSesionProfesor():
	session['AUTH'] = 'Vacio'
	session['id'] = None
	session['username'] = None
	session['nombre'] = None
	return redirect("/profesor")
