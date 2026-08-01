from datetime import date
from database import db

#qa approved :p

class Empleado(db.Model):
    __tablename__ = "empleados"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    puesto = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False, default=0.0)
    fecha_ingreso = db.Column(db.Date, nullable=False, default=date.today)

    def to_dict(self):
        fecha_formateada = ""
        if self.fecha_ingreso:
            fecha_formateada = self.fecha_ingreso.strftime("%d/%m/%Y")

        return {
            "id": self.id,
            "nombre": self.nombre,
            "puesto": self.puesto,
            "salario": self.salario,
            "fecha_ingreso": fecha_formateada,
        }
