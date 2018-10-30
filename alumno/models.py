from app import db

class Alumno(db.Model):
    idAlumno = db.Column(db.Integer, primary_key=True)
    usuarioAlumno = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    #carrera = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Alumno %r>' % self.usuarioAlumno


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
    
class registroSeminario(db.Model):
    idRegistroSeminario = db.Column(db.Integer, primary_key=True)
    idSeminario = db.Column(db.Integer, db.ForeignKey('seminario.idSeminario'), nullable=False)
    seminario = db.relationship('Seminario', backref=db.backref('seminarios', lazy=True))
    idAlumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'), nullable=False)
    alumno = db.relationship('Seminario', backref=db.backref('alumnos', lazy=True))

    def __repr__(self):
        return '<RegistroSeminario %r>' % self.idRegistroSeminario
