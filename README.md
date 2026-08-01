# CRUD Empleados

Aplicación web sencilla en **Python + Flask** para gestionar empleados
(Crear, Leer, Actualizar, Eliminar), pensada para abrirse directamente en
**PyCharm** como proyecto.

## Requisitos
- Python 3.10+
- PyCharm (Community o Professional)

## Instalación

```bash
python -m venv .venv
# Windows (Git Bash): source .venv/Scripts/activate
# Windows (CMD/PowerShell): .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
```

## Base de datos

Por defecto el proyecto usa **SQLite** (archivo `empleados.db`, no requiere
instalar nada). Para usar **SQL Server**:

1. Instala el driver ODBC 17 de SQL Server en tu máquina.
2. Descomenta `pyodbc` en `requirements.txt` e instala con `pip install -r requirements.txt`.
3. Define las variables de entorno antes de ejecutar (o edítalas directamente en `config.py`):

```bash
export DB_ENGINE=sqlserver
export SQLSERVER_HOST=localhost
export SQLSERVER_DB=CrudEmpleadosDB
export SQLSERVER_USER=sa
export SQLSERVER_PASSWORD=TuPasswordAqui
```

## Ejecutar

```bash
python app.py
```

Luego abre http://127.0.0.1:5000 en el navegador. Te pedirá iniciar sesión:

- **Usuario:** `admin`
- **Contraseña:** `admin123`

(Credenciales de demostración, definidas en `routes.py`. En un proyecto real
irían en variables de entorno con contraseñas hasheadas.)

## Funcionalidades

- **Login** (`/login`) protege todas las rutas de gestión de empleados.
- **CRUD completo** de empleados: crear, listar, editar, eliminar.
- **Validación de datos** en el servidor (nombre/puesto mínimo 2 caracteres,
  salario positivo, fecha de ingreso no futura).
- **Dashboard** (`/dashboard`) con estadísticas: total de empleados, salario
  promedio, salario más alto, puestos distintos.
- **API JSON** (`/api/empleados` y `/api/empleados/<id>`) para integrarse con
  otros sistemas.

## Estructura del proyecto

```
crud-empleados/
├── app.py          # Punto de entrada de la aplicación
├── config.py       # Configuración de la base de datos
├── database.py     # Instancia de SQLAlchemy
├── models.py       # Modelo Empleado
├── routes.py        # Rutas CRUD (Blueprint)
├── templates/       # Vistas HTML (Jinja2)
├── static/          # CSS
└── requirements.txt
```
