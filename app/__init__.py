"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Creating Apps"""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    SECRET_KEY = os.urandom(32)
    app.secret_key = SECRET_KEY
    
    # Database Config
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = ""


    # Initialize
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Web application routes (auth / main)
        from . import routes
        from . import auth

        # Register Blueprints
        app.register_blueprint(routes.main_pages)
        app.register_blueprint(auth.auth_pages)

        # Create Database Models
        db.create_all()

        return app
