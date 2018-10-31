from utils import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

from alumno.models import *
from profesor.models import *

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
			session['AUTH'] = None
			return render_template('profesor/login.html', val = False)
	else:
		session['AUTH'] = 'Vacio'
		return render_template('profesor/login.html', val = False)
	


@app.route("/profesor/login", methods=['POST'])
def loginProfesor():
	pw = encode(request.form['uname'], request.form['psw'])
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
			session['AUTH'] = None
			return redirect("/profesor")
	else:
		session['AUTH'] = None
		return redirect("/profesor")
	
	
@app.route("/profesor/editarDisponibilidad/<int:id>")	
def editarDisponibilidadProfesor(id):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			asesoria = Asesoria.query.filter_by(idAsesoria=id).first()
			if asesoria.disponibilidad == "No Disponible":
				asesoria.disponibilidad == "Disponible"
			else:
				asesoria.disponibilidad == "No Disponible"
			db.session.commit()
			return redirect('/profesor/displayProximasAsesorias')
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = None
			return redirect("/profesor")
	else:
		session['AUTH'] = None
		return redirect("/profesor")
	
	
@app.route("/profesor/displayProximasAsesoriasDetalle/<int:id>")
def detalleAsesoriasProfesor(id):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			citas = Cita.query.filter_by(idAsesoria=id).all()
			username = session['username']
			return render_template('profesor/proximasAsesoriasDetalle.html', citas=citas, usuario=username)
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = None
			return redirect("/profesor")
	else:
		session['AUTH'] = None
		return redirect("/profesor")

@app.route("/profesor/displayHistorial")
def historialProfesor():
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			profesor = Profesor.query.filter_by(usuarioProfesor=session['username']).first()
			username = session['username']
			fecha = datetime.date.today()
			return render_template('profesor/historialProfesor.html', profesor=profesor, fecha=fecha, usuario=username)
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = None
			return redirect("/profesor")
	else:
		session['AUTH'] = None
		return redirect("/profesor")
	
@app.route("/profesor/displayHistorialDetalle/<int:id>")
def detalleHistorialProfesor(id):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			asesoria = Asesoria.query.filter_by(idAsesoria=id).first()
			username = session['username']
			return render_template('profesor/historialDetalleProfesor.html', asesoria=asesoria, usuario=username)
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			return redirect('/administrador')
		else:
			session['AUTH'] = None
			return redirect("/profesor")
	else:
		session['AUTH'] = None
		return redirect("/profesor")


@app.route("/profesor/cerrarSesion")
def cerrarSesionProfesor():
	session['AUTH'] = 'Vacio'
	session['id'] = None
	session['username'] = None
	session['nombre'] = None
	return redirect("/profesor")
