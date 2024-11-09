from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
import auth

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poll_app.db' 
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    login_manager.init_app(app)

    # import all the model definitions after initializing db
    with app.app_context():
        import models
        db.create_all()

    # Specify the view/function where users are redirected to if not logged in
    login_manager.login_view = 'homepage'

    return app



app = create_app()

@app.route("/")
def homepage():
    return render_template("hello world")

from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return auth.load_user(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if (auth.login(email, password)): # login succeeded
            return redirect(url_for("dashboard"))
    return render_template("Login page")


@app.route('/logout')
@login_required
def logout():
    auth.logout()
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if (auth.signup(email, password)):
            return redirect(url_for("dashboard"))
    return render_template("Signup page")



@app.route('/dashboard')
@login_required
def dashboard():
    return "This is a protected page"


if (__name__ == "__main__"):
    app.run()

