from functools import wraps
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from database import db
from models import Empleado

empleados_bp = Blueprint("empleados", __name__)

DEMO_USUARIO = "admin"
DEMO_PASSWORD = "admin123"


def login_required(f):
    """Protege una ruta exigiendo que exista una sesión iniciada."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"):
            flash("Debes iniciar sesión para continuar.", "error")
            return redirect(url_for("empleados.login"))
        return f(*args, **kwargs)
    return wrapper


# ---------------------------- LOGIN / LOGOUT ----------------------------
@empleados_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "")
        if usuario == DEMO_USUARIO and password == DEMO_PASSWORD:
            session["usuario"] = usuario
            flash(f"Bienvenido, {usuario}.", "success")
            return redirect(url_for("empleados.index"))
        flash("Usuario o contraseña incorrectos.", "error")
    return render_template("login.html")


@empleados_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Sesión cerrada.", "success")
    return redirect(url_for("empleados.login"))


# ---------------------------- READ ----------------------------
@empleados_bp.route("/")
@login_required
def index():
    empleados = Empleado.query.order_by(Empleado.id).all()
    return render_template("index.html", empleados=empleados)


def validar_datos_empleado(nombre, puesto, salario, fecha_ingreso):
    """Valida los datos del formulario de empleado. Devuelve una lista de errores."""
    errores = []
    if not nombre or len(nombre) < 2:
        errores.append("El nombre debe tener al menos 2 caracteres.")
    if not puesto or len(puesto) < 2:
        errores.append("El puesto debe tener al menos 2 caracteres.")
    try:
        if float(salario) <= 0:
            errores.append("El salario debe ser mayor que 0.")
    except (TypeError, ValueError):
        errores.append("El salario debe ser un número válido.")
    if fecha_ingreso:
        try:
            fecha = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
            if fecha > datetime.today().date():
                errores.append("La fecha de ingreso no puede ser futura.")
        except ValueError:
            errores.append("La fecha de ingreso no tiene un formato válido.")
    return errores


# ---------------------------- CREATE ----------------------------
@empleados_bp.route("/crear", methods=["GET", "POST"])
@login_required
def crear():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        puesto = request.form.get("puesto", "").strip()
        salario = request.form.get("salario", "0")
        fecha_ingreso = request.form.get("fecha_ingreso")

        errores = validar_datos_empleado(nombre, puesto, salario, fecha_ingreso)
        if errores:
            for e in errores:
                flash(e, "error")
            return redirect(url_for("empleados.crear"))

        nuevo = Empleado(
            nombre=nombre,
            puesto=puesto,
            salario=float(salario or 0),
            fecha_ingreso=datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
            if fecha_ingreso else datetime.today().date(),
        )
        db.session.add(nuevo)
        db.session.commit()
        flash("Empleado creado correctamente.", "success")
        return redirect(url_for("empleados.index"))

    return render_template("create.html")


# ---------------------------- UPDATE ----------------------------
@empleados_bp.route("/editar/<int:empleado_id>", methods=["GET", "POST"])
@login_required
def editar(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        puesto = request.form.get("puesto", "").strip()
        salario = request.form.get("salario", "0")
        fecha_ingreso = request.form.get("fecha_ingreso")

        errores = validar_datos_empleado(nombre, puesto, salario, fecha_ingreso)
        if errores:
            for e in errores:
                flash(e, "error")
            return redirect(url_for("empleados.editar", empleado_id=empleado_id))

        empleado.nombre = nombre
        empleado.puesto = puesto
        empleado.salario = float(salario)
        if fecha_ingreso:
            empleado.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()

        db.session.commit()
        flash("Empleado actualizado correctamente.", "success")
        return redirect(url_for("empleados.index"))

    return render_template("edit.html", empleado=empleado)


# ---------------------------- DASHBOARD ----------------------------
@empleados_bp.route("/dashboard")
@login_required
def dashboard():
    empleados = Empleado.query.all()
    total = len(empleados)
    salario_promedio = sum(e.salario for e in empleados) / total if total else 0
    salario_max = max((e.salario for e in empleados), default=0)
    puestos_unicos = len({e.puesto for e in empleados})
    return render_template(
        "dashboard.html",
        total=total,
        salario_promedio=salario_promedio,
        salario_max=salario_max,
        puestos_unicos=puestos_unicos,
    )


# ---------------------------- DELETE ----------------------------
@empleados_bp.route("/eliminar/<int:empleado_id>", methods=["POST"])
@login_required
def eliminar(empleado_id):
    empleado = Empleado.query.get_or_404(empleado_id)
    db.session.delete(empleado)
    db.session.commit()
    flash("Empleado eliminado correctamente.", "success")
    return redirect(url_for("empleados.index"))
