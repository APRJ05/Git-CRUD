# CRUD Empleados

## Requisitos
- Python 3.10+
- PyCharm (Community o Professional)

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
