from flask_login import login_required
from flask import request, redirect, url_for, render_template
from app import create_app, login_manager
from app import auth

app = create_app()

@app.route("/")
def homepage():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    return auth.load_user(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(f"login called with method {request.method}")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"email is {email}")
        print(f"password is {password}")
        if (auth.login(email, password)): # login succeeded
            return redirect(url_for("dashboard"))
    return render_template("login.html")

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
    return render_template("signup.html")

@app.route('/dashboard')
@login_required
def dashboard():
    return "This is a protected page"
