from app import db

class Profesor(db.Model):
    idProfesor = db.Column(db.Integer, primary_key=True)
    usuarioProfesor = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    carrera = db.Column(db.String, nullable=False)
    #foto = db.Column(db.String, nullable=False)

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
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.String, nullable=False)
    lugar = db.Column(db.String, nullable=False)
    disponibilidad = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Asesoria %r>' % self.idAsesoria

class Seminario(db.Model):
    idSeminario = db.Column(db.Integer, primary_key=True)
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    profesor = db.relationship('Profesor', backref=db.backref('profesor', lazy=True))
    topic = db.Column(db.String, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.String, nullable=False)
    lugar = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Seminario %r>' % self.idSeminario
