from db import db
from sqlalchemy import text

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)
    telefono = db.Column(db.Integer,nullable=False)

    perro = db.relationship('Perro', back_populates="cuidador", single_parent=True, cascade="all,delete-orphan")