from db import db
from sqlalchemy import text

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)
    raza = db.Column(db.String(20),nullable=False)
    edad = db.Column(db.Integer,nullable=False)
    peso = db.Column(db.Integer,nullable=False)
    idcuidador = db.Column(db.Integer,db.ForeignKey(Cuidador.id),nullable=False)

    cuidador = db.relationship('Cuidador', uselist=False,
                               back_populates="perro", cascade="all, delete-orphan", single_parent=True)
