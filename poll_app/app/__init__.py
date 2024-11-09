import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///poll_app.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()

    login_manager.login_view = 'homepage'
    return app
