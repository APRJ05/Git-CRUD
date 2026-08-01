from flask import Flask

from config import Config
from database import db
from routes import empleados_bp
from api import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(empleados_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()  # crea las tablas si no existen

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
