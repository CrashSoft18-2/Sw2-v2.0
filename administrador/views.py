from utils import *
from alumno.models import *
from profesor.models import *
from administrador.models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime
from datetime import datetime as dt
import json
import pytz

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
			return render_template('administrador/programarAsesorias.html', usuario=username)
		else:
			session['AUTH'] = 'Vacio'
			return render_template('administrador/login.html')
	else:
		session['AUTH'] = 'Vacio'
		return redirect("/alumno")

@app.route("/administrador/agregarAsesoria/<int:id>", methods=['POST'])
def crearNuevaAsesoriaAdm(id):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Administrador':
			username = session['username']
			asesoria = Asesoria(idProfesor=id,fecha=request.form['fecha'],hora=request.form['hora'],lugar=request.form['lugar'],disponibilidad="Disponible")
			db.session.add(asesoria)
			db.session.commit()
			return redirect('/administrador/displayAsesoriasDetalle/' + str(id))
		else:
			session['AUTH'] = 'Vacio'
			return render_template('administrador/login.html')
	else:
		session['AUTH'] = 'Vacio'
		return redirect("/alumno")

@app.route("/administrador/eliminarAsesoria/<int:idProfesor>/<int:idAsesoria>")
def eliminarAsesoriaAdm(idProfesor, idAsesoria):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			asesoria = Asesoria.query.filter_by(idAsesoria=idAsesoria).first()
			db.session.delete(asesoria)
			db.session.commit()
			return redirect('/administrador/displayAsesoriasDetalle/' + str(idProfesor))
		else:
			session['AUTH'] = None
			return redirect("/administrador")
	else:
		session['AUTH'] = None
		return redirect("/administrador")

@app.route("/administrador/editarAsesoria/<int:idProfesor>/<int:idAsesoria>")
def prepararParaEditarAsesoriaAdm(idProfesor, idAsesoria):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			profesor = Profesor.query.filter_by(idProfesor=idProfesor).first()
			fecha = datetime.date.today()
			username = session['username']
			return render_template('administrador/detalleProfesor.html', profesor=profesor, fecha=fecha, usuario=username, editar=idAsesoria)
		else:
			session['AUTH'] = None
			return redirect("/administrador")
	else:
		session['AUTH'] = None
		return redirect("/administrador")

@app.route("/administrador/commitEditarAsesoria/<int:idProfesor>/<int:idAsesoria>", methods=['POST'])
def editarAsesoriaAdm(idProfesor, idAsesoria):
	if session.get('AUTH') != None:
		if session['AUTH'] == 'Profesor':
			return redirect('/profesor')
		elif session['AUTH'] == 'Alumno':
			return redirect('/alumno')
		elif session['AUTH'] == 'Administrador':
			asesoria = Asesoria.query.filter_by(idAsesoria=idAsesoria).first()
			asesoria.fecha = request.form['fecha']
			asesoria.hora = request.form['hora']
			asesoria.lugar = request.form['lugar']
			db.session.commit()
			return redirect('/administrador/displayAsesoriasDetalle/' + str(idProfesor))
		else:
			session['AUTH'] = None
			return redirect("/administrador")
	else:
		session['AUTH'] = None
		return redirect("/administrador")

@app.route("/administrador/programarAsesorias", methods=['POST'])
def programarAsesoriasAdmMasivo():
	data_from_request = request.form.to_dict()
	top = dt.strptime(data_from_request["date"], "%Y-%m-%d")
	weekday_hoy = int(datetime.datetime.now(pytz.timezone('America/Lima')).weekday())
	for i in range(6):
		key = "dia" + str(i + 1)
		date = datetime.datetime.now(pytz.timezone('America/Lima'))
		if key in data_from_request:
			weekday_target = int(data_from_request[key])
			cantidad_de_dias = getCantidadDias(weekday_hoy, weekday_target)
			fecha_inicio = date + datetime.timedelta(days=cantidad_de_dias)
			while date < top:
				//programarAsesorias
				print(date)
				date += datetime.timedelta(days=7)
	return ""

@app.route("/administrador/cerrarSesion")
def cerrarSesionAdm():
	session['AUTH'] = None
	session['id'] = None
	session['username'] = None
	session['nombre'] = None
	return redirect("/administrador")
