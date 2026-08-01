from flask import Blueprint, jsonify

from models import Empleado

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/empleados", methods=["GET"])
def listar_empleados_json():

    empleados = Empleado.query.order_by(Empleado.id).all()
    return jsonify([e.to_dict() for e in empleados])


@api_bp.route("/empleados/<int:empleado_id>", methods=["GET"])
def obtener_empleado_json(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)
    return jsonify(empleado.to_dict())

# Github desktop the best 