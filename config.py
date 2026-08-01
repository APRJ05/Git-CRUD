import os

DB_ENGINE = os.environ.get("DB_ENGINE", "sqlite")  # "sqlite" o "sqlserver"

# --- Configuración para SQL Server (requiere: pip install pyodbc) ---
SQLSERVER_DRIVER = os.environ.get("SQLSERVER_DRIVER", "ODBC Driver 17 for SQL Server")
SQLSERVER_HOST = os.environ.get("SQLSERVER_HOST", "localhost")
SQLSERVER_DB = os.environ.get("SQLSERVER_DB", "CrudEmpleadosDB")
SQLSERVER_USER = os.environ.get("SQLSERVER_USER", "sa")
SQLSERVER_PASSWORD = os.environ.get("SQLSERVER_PASSWORD", "TuPasswordAqui")


def get_database_uri() -> str:
    if DB_ENGINE == "sqlserver":
        return (
            f"mssql+pyodbc://{SQLSERVER_USER}:{SQLSERVER_PASSWORD}"
            f"@{SQLSERVER_HOST}/{SQLSERVER_DB}"
            f"?driver={SQLSERVER_DRIVER.replace(' ', '+')}"
        )
    # SQLite por defecto: crea un archivo local empleados.db
    return "sqlite:///empleados.db"


class Config:
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave-secreta-desarrollo")
