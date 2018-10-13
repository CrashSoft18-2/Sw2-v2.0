import base64
from firebase_admin import credentials
from firebase_admin import db as dbFirebase
import firebase_admin
import os

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def connectToFirebase():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_URL = SITE_ROOT + '/static/json/login.json'
	if (not len(firebase_admin._apps)):
		cred = credentials.Certificate(json_URL)
		firebase_admin.initialize_app(cred, {'databaseURL' : 'https://crashsoft-e0a3e.firebaseio.com/'})
		
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
		redirect('/index')
	else:
		return render_template('login.html', val = True)
