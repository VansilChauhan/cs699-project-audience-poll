from poll_secrets import db_uri, db_secret_key, admins
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'index'


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = db_secret_key

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()
        from app import auth
        auth.add_admins(admins)
        user_count=20
        for i in range(user_count//2):
            auth.signup(email=f"mstudent{i}@example.com", password="123ABCabc#", age=24, gender="male")
            auth.signup(email=f"fstudent{i+user_count//2}@example.com", password="123ABCabc#", age=24, gender="female")
    return app
