from app import db

class Alumno(db.Model):
    idAlumno = db.Column(db.Integer, primary_key=True)
    usuarioAlumno = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    carrera = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Alumno %r>' % self.usuarioAlumno
