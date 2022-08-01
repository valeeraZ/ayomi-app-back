"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import get_config
import pymysql
pymysql.install_as_MySQLdb()

cors = CORS()
db = SQLAlchemy()
# migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask("flask-authentication")
    app.config.from_object(get_config(config_name))

    from .api import api_bp

    app.register_blueprint(api_bp)

    cors.init_app(app)
    db.init_app(app)
    # migrate.init_app(app, db)
    bcrypt.init_app(app)
    return app
