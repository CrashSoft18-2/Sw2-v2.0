from utils import *
from alumno.models import *
from flask import session, request, render_template, url_for, redirect

import datetime

@app.route("/")
def inicio():
	if session.get('AUTH') != None:
		if session['AUTH'] == True:
			return index()
		else:
			session['AUTH'] = False
			return render_template('alumno/login.html', val = session['AUTH'])
	else:
		session['AUTH'] = False
		return render_template('alumno/login.html', val = session['AUTH'])

@app.route('/profesor/<int:id>')
def profesor(id):
	if session.get('AUTH') == True:
		profesor = Profesor.query.filter_by(idProfesor=id).first()
		date = Asesoria.query.filter_by(idProfesor=id).first().fecha
		fecha = datetime.date.today()
		return render_template('alumno/detalleProfesor.html', profesor=profesor, fecha=fecha)
	else:
		return inicio()

@app.route('/misCitas')
def citas():
	if session.get('AUTH') == True:
		alumnoid = session['id']
		citas = Cita.query.filter_by(idAlumno=alumnoid)
		return render_template('alumno/misCitas.html', citas=citas)
	else:
		return inicio()

@app.route('/detalleHistorial/<id>')
def detalleHistorial(id):
	if session.get('AUTH') == True:
		profesor = Profesor.query.filter_by(idProfesor=int(id)).first()
		fecha = datetime.date.today()
		return render_template('alumno/detalleHistorial.html', profesor=profesor, fecha=fecha)
	else:
		return inicio()
	

@app.route('/temasHistorial/<id>')
def temasHistorial(id):
	if session.get('AUTH') == True:
		asesoria = Asesoria.query.filter_by(idAsesoria=int(id)).first()
		print(asesoria)
		return render_template('alumno/temasHistorial.html', asesoria=asesoria)
	else:
		return inicio()
	
@app.route('/historial')
def historial():
	if session.get('AUTH') == True:
		profesores = Profesor.query.all()
		return render_template('alumno/historial.html', profesores=profesores)
	else:
		return inicio()

@app.route('/login', methods=['POST'])
def login():
	pw = encode(request.form['uname'], request.form['psw'])
	alumno = Alumno.query.filter_by(usuarioAlumno=request.form['uname'], contrasena=pw).first()
	if alumno:
		session['AUTH'] = True
		session['id'] = alumno.idAlumno
		session['username'] = alumno.usuarioAlumno
		session['nombre'] = alumno.nombre
		return index()
	else:
		return render_template('alumno/login.html', val = True)
  
@app.route("/index")
def index():
	if session.get('AUTH') == True:
		profesores = Profesor.query.all()
		return render_template('alumno/index.html', profesores=profesores)
	else:
		return inicio()

@app.route("/reservarCita/<int:idAs>")
def reservarCita(idAs):
	if session.get('AUTH') == True:
		session['idAs'] = idAs
		asesoria = Asesoria.query.filter_by(idAsesoria=idAs).first()
		return render_template('alumno/reservarCita.html', asesoria=asesoria)
	else:
		return inicio()

@app.route("/generarReserva", methods=['POST'])
def generarReserva():
	if session.get('AUTH') == True:
		fecha = datetime.date.today()
		cita = Cita(idAlumno=session['id'], idAsesoria=session['idAs'], fecha=fecha, pregunta=request.form['consulta'])
		db.session.add(cita)
		db.session.commit()
		asesoria = Asesoria.query.filter_by(idAsesoria=session['idAs']).first()
		return render_template('alumno/reservarCita.html', asesoria=asesoria)
	else:
		return inicio()

@app.route("/cancelarReserva/<int:id>")
def cancelarReserva(id):
	cita = Cita.query.filter_by(idCita = id).first()
	db.session.delete(cita)
	db.session.commit()
	return redirect('/misCitas')

@app.route("/seminarios")
def seminarios():
	seminarios = Seminario.query.order_by(seminario.fecha)
	return render_template('alumno/seminarios.html', seminarios=seminarios)

@app.route("/cerrarSesion")
def cerrarSesion():
	session['AUTH'] = False
	return inicio()
