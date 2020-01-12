"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import urllib.parse
import pyodbc

# Database Setting
db = SQLAlchemy()

server = 'mysqlserver-nwhacks.database.windows.net'
database = 'mysampledatabase'
username = 'azureuser'
password = 'HELLO-world'
driver= '{ODBC Driver 17 for SQL Server}'
DATABASE_URI = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password

params = urllib.parse.quote_plus(DATABASE_URI)


login_manager = LoginManager()


def create_app():
    """Creating Apps"""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    SECRET_KEY = os.urandom(32)
    app.secret_key = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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
