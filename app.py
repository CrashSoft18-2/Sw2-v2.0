from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from firebase_admin import credentials
from firebase_admin import db as dbFirebase
import firebase_admin
import os
import psycopg2
from flask import session
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://inrbkbfqwjvcnb:83df34940918d53940c4bd30b5a185d3d79726cd36230f4a402f4a8f8579e680@ec2-174-129-35-61.compute-1.amazonaws.com:5432/da8gvk43j45moa'#'postgres://postgres:postgres@localhost:5432/test'
app.secret_key = b'1234'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from models import *

class Test():
	pass

def test():
	print(Alumno.query.all())

@app.route("/")
def inicio():
	Test.AUTH = False
	return render_template('login.html', val = Test.AUTH)

@app.route('/profesor/<int:id>')
def profesor(id):
	profesor = Profesor.query.filter_by(idProfesor=id).first()
	return render_template('detalleProfesor.html', profesor=profesor)


@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		alumno = Alumno.query.filter_by(usuarioAlumno=request.form['uname'], contrasena=request.form['psw']).first()
		if alumno:
			Test.AUTH = True
			session['id'] = alumno.idAlumno
			session['username'] = alumno.usuarioAlumno
			session['nombre'] = alumno.nombre
			return index()
		else:
			return render_template('login.html', val = True)

def do_the_login():
	connectToFirebase()
	nodo_raiz = dbFirebase.reference()
	lista_alumnos = nodo_raiz.child('Usuarios/Alumnos').get()
	lista_docentes = nodo_raiz.child('Usuarios/Profesores').get()
	Test.AUTH = False
	for alumno in lista_alumnos:
		usuario = str(alumno.get("user"))
		password = str(alumno.get("password"))
		postUsuario = request.form['uname'] + ""
		postPassword = request.form['psw'] + ""
		if (usuario == postUsuario and password == postPassword):
			Test.AUTH = True
			print(Test.AUTH)
			break
	if Test.AUTH == True:
		session['username'] = request.form['uname']
		return index()
	else:
		return render_template('login.html', val = True)

@app.route("/index")
def index():
	if (Test.AUTH == True):
		profesores = Profesor.query.all()
		citas = Cita.query.all()
		return render_template('index.html', profesores=profesores, citas=citas)
	else:
		return render_template('login.html', val = Test.AUTH)

@app.route("/reservarCita/<int:idAs>")
def reservarCita(idAs):
	session['idAs'] = idAs
	asesoria = Asesoria.query.filter_by(idAsesoria=idAs).first()
	return render_template('reservarCita.html', asesoria=asesoria)

@app.route("/generarReserva", methods=['POST'])
def generarReserva():
	fecha = datetime.now().date()
	cita = Cita(idAlumno=session['id'], idAsesoria=session['idAs'], fecha=fecha, pregunta=request.form['consulta'])
	db.session.add(cita)
	db.session.commit()
	asesoria = Asesoria.query.filter_by(idAsesoria=session['idAs']).first()
	return render_template('reservarCita.html', asesoria=asesoria)

def connectToFirebase():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_URL = SITE_ROOT + '/static/json/login.json'
	if (not len(firebase_admin._apps)):
		cred = credentials.Certificate(json_URL)
		firebase_admin.initialize_app(cred, {'databaseURL' : 'https://crashsoft-e0a3e.firebaseio.com/'})

#def connectToPostgres():
	#

def init():
    #port = int(os.environ.get('PORT', 5000))
    app.run()
    #app.run(host='0.0.0.0', port=port, debug=True)
	#firebase_admin.initialize_app()

if __name__ == "__main__":
	init()
	#main()
