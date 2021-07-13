from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.endereco_model import Endereco
    from app.models.clientes_mode import Clientes
