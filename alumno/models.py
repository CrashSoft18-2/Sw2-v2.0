from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Alumno(db.Model):
    idAlumno = db.Column(db.Integer, primary_key=True)
    usuarioAlumno = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Alumno %r>' % self.usuarioAlumno

class Profesor(db.Model):
    idProfesor = db.Column(db.Integer, primary_key=True)
    usuarioProfesor = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    carrera = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Profesor %r>' % self.usuarioProfesor

class Curso(db.Model):
    idCurso = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Curso %r>' % self.nombre

class Seccion(db.Model):
    idSeccion = db.Column(db.Integer, primary_key=True)
    idCurso = db.Column(db.Integer, db.ForeignKey('curso.idCurso'), nullable=False)
    curso = db.relationship('Curso', backref=db.backref('seccions', lazy=True))
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    profesor = db.relationship('Profesor', backref=db.backref('seccions', lazy=True))
    numeroSeccion = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Seccion %r>' % self.numeroSeccion

class Asesoria(db.Model):
    idAsesoria = db.Column(db.Integer, primary_key=True)
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    profesor = db.relationship('Profesor', backref=db.backref('asesorias', lazy=True))
    fecha = db.Column(db.Date, nullable=False) #fecha??
    hora = db.Column(db.String, nullable=False) #hora??
    lugar = db.Column(db.String, nullable=False)
    disponibilidad = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Asesoria %r>' % self.idAsesoria

class Cita(db.Model):
    idCita = db.Column(db.Integer, primary_key=True)
    idAlumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'), nullable=False)
    alumno = db.relationship('Alumno', backref=db.backref('citas', lazy=True))
    idAsesoria = db.Column(db.Integer, db.ForeignKey('asesoria.idAsesoria'), nullable=False)
    asesoria = db.relationship('Asesoria', backref=db.backref('citas', lazy=True))
    fecha = db.Column(db.Date, nullable=False) #fecha??
    pregunta = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Cita %r>' % self.idCita

class Registro(db.Model):
    idRegistro = db.Column(db.Integer, primary_key=True)
    idAsesoria = db.Column(db.Integer, db.ForeignKey('asesoria.idAsesoria'), nullable=False)
    asesoria = db.relationship('Asesoria', backref=db.backref('registros', lazy=True))
    temaTratado = db.Column(db.String, nullable=False)
    conclusion = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Registro %r>' % self.idRegistro
    
class Seminario(db.Model):
    idSeminario = db.Column(db.Integer, primary_key=True)
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    profesor = db.relationship('Profesor', backref=db.backref('profesor', lazy=True))
    carrera = db.Column(db.String, nullable=False)
    topic = db.Column(db.String, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.String, nullable=False)
    lugar = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Seminario %r>' % self.idSeminario
    
class registroSeminario(db.Model):
    idRegistroSeminario = db.Column(db.Integer, primary_key=True)
    idSeminario = db.Column(db.Integer, db.ForeignKey('seminario.idSeminario'), nullable=False)
    seminario = db.relationship('Seminario', backref=db.backref('seminarios', lazy=True))
    idAlumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'), nullable=False)
    alumno = db.relationship('Seminario', backref=db.backref('alumnos', lazy=True))

    def __repr__(self):
        return '<RegistroSeminario %r>' % self.idRegistroSeminario
