from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
import datetime

@app.route("/")
def select():
	if session.get('AUTH') != None:
		if session['AUTH'] == True:
			return index()
		else:
			session['AUTH'] = False
			return render_template('index.html')
	else:
		session['AUTH'] = False
		return render_template('index.html')
  

@app.route("/alumno")
def inicio():
	if session.get('AUTH') != None:
		if session['AUTH'] == True:
			return index()
		else:
			session['AUTH'] = False
			return render_template('alumno/login.html')
	else:
		session['AUTH'] = False
		return render_template('alumno/login.html')

	
@app.route("/alumno/login", methods=['POST'])
def loginAlumno():
	pw = encode(request.form['uname'], request.form['psw'])
	alumno = Alumno.query.filter_by(usuarioAlumno=request.form['uname'], contrasena=pw).first()
	if alumno:
		session['AUTH'] = True
		session['type'] = "ALUMNO"
		session['id'] = alumno.idAlumno
		session['username'] = alumno.usuarioAlumno
		session['nombre'] = alumno.nombre
		return redirect("/alumno/displayAsesorias")
	else:
		return render_template('alumno/login.html', val = True)


@app.route("/alumno/displayAsesorias")
def index():
	if session.get('AUTH') == True:
		profesores = Profesor.query.all()
		username = session['username']
		return render_template('alumno/index.html', profesores=profesores, usuario=username)
	else:
		return inicio()

	
@app.route("/alumno/displayProfesor/<int:id>")
def profesor(id):
	if session.get('AUTH') == True:
		profesor = Profesor.query.filter_by(idProfesor=id).first()
		date = Asesoria.query.filter_by(idProfesor=id).first().fecha
		fecha = datetime.date.today()
		username = session['username']
		return render_template('alumno/detalleProfesor.html', profesor=profesor, fecha=fecha, usuario=username)
	else:
		return inicio()

	
@app.route("/alumno/reservarCita/<int:idAs>")
def reservarCita(idAs):
	if session.get('AUTH') == True:
		session['idAs'] = idAs
		asesoria = Asesoria.query.filter_by(idAsesoria=idAs).first()
		username = session['username']
		return render_template('alumno/reservarCita.html', asesoria=asesoria, usuario=username)
	else:
		return inicio()
	
	
@app.route("/alumno/generarReserva", methods=['POST'])
def generarReserva():
	if session.get('AUTH') == True:
		fecha = datetime.date.today()
		cita = Cita(idAlumno=session['id'], idAsesoria=session['idAs'], fecha=fecha, pregunta=request.form['consulta'])
		db.session.add(cita)
		db.session.commit()
		username = session['username']
		asesoria = Asesoria.query.filter_by(idAsesoria=session['idAs']).first()
		return render_template('alumno/reservarCita.html', asesoria=asesoria, usuario=username)
	else:
		return inicio()

	
@app.route("/alumno/displayHistorial")
def historial():
	if session.get('AUTH') == True:
		profesores = Profesor.query.all()
		username = session['username']
		return render_template('alumno/historial.html', profesores=profesores, usuario=username)
	else:
		return inicio()

	
@app.route('/alumno/detalleHistorial/<id>')
def detalleHistorial(id):
	if session.get('AUTH') == True:
		profesor = Profesor.query.filter_by(idProfesor=int(id)).first()
		fecha = datetime.date.today()
		username = session['username']
		return render_template('alumno/detalleHistorial.html', profesor=profesor, fecha=fecha, usuario=username)
	else:
		return inicio()
	

@app.route("/alumno/temasHistorial/<id>")
def temasHistorial(id):
	if session.get('AUTH') == True:
		asesoria = Asesoria.query.filter_by(idAsesoria=int(id)).first()
		username = session['username']
		return render_template('alumno/temasHistorial.html', asesoria=asesoria, usuario=username)
	else:
		return inicio()
	
	
@app.route("/alumno/displayMisCitas")
def citas():
	if session.get('AUTH') == True:
		alumnoid = session['id']
		citas = Cita.query.filter_by(idAlumno=alumnoid)
		username = session['username']
		return render_template('alumno/misCitas.html', citas=citas, usuario=username)
	else:
		return inicio()


@app.route("/alumno/cancelarReserva/<int:id>")
def cancelarReserva(id):
	if session.get('AUTH') == True:
		cita = Cita.query.filter_by(idCita = id).first()
		db.session.delete(cita)
		db.session.commit()
		return redirect('/alumno/displayMisCitas')
	else:
		return inicio()

	
@app.route("/alumno/displaySeminarios")
def seminarios():
	if session.get('AUTH') == True:
		seminarios = Seminario.query.order_by(Seminario.fecha, Seminario.hora).all()
		username = session['username']
		return render_template('alumno/seminarios.html', seminarios=seminarios, usuario=username)
	else:
		return inicio()
	
@app.route("/alumno/inscripcionSeminario/<int:id>")
def inscripcion(id):
	if session.get('AUTH') == True:
		registro = registroSeminario(idAlumno=session['id'], idSeminario=id)
		db.session.add(registro)
		db.session.commit()
		return seminarios()
	else:
		return inicio()

@app.route("/alumno/displayMisSeminarios")
def registroSeminarios():
	if session.get('AUTH') == True:
		seminarios = registroSeminario.query.filter_by(idAlumno=session['id']).join(Seminario).order_by(Seminario.fecha, Seminario.hora).all()
		username = session['username']
		return render_template('alumno/misSeminarios.html', registros=seminarios, usuario=username)
	else:
		return inicio()	

@app.route("/alumno/cancelarSeminario/<int:id>")
def cancelarSeminario(id):
	if session.get('AUTH') == True:
		registro = registroSeminario.query.filter_by(idRegistroSeminario=id).first()
		db.session.delete(registro)
		db.session.commit()
		return registroSeminarios()
	else:
		return inicio()

@app.route("/alumno/cerrarSesion")
def cerrarSesion():
	session['AUTH'] = False
	return inicio()
