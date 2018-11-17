from app import db

class Administrador(db.Model):
    idAdministrador = db.Column(db.Integer, primary_key=True)
    usuarioAdministrador = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Administrador %r>' % self.usuarioAdministrador

