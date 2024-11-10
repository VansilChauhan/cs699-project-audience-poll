from flask_login import login_required
from flask_login import current_user
from flask import request, redirect, url_for, render_template
from app import create_app, login_manager
from app import auth
from app import poll_service as ps


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
            return redirect(url_for("feed"))
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
            return redirect(url_for("feed"))
    return render_template("signup.html")

@app.route('/feed')
@login_required
def feed():
    return render_template("feed.html")

@app.route('/create_poll', methods=['GET', 'POST'])
@login_required
def create_poll():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        poll = ps.create_poll(title=title, description=description, creator_id=current_user.id)
        ps.create_option(text=request.form['option1'], poll_id=poll.id)
        ps.create_option(text=request.form['option2'], poll_id=poll.id)
    return render_template("create_poll.html")