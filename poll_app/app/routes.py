import qrcode
from io import BytesIO
import base64
from flask_login import login_required, current_user
from flask import request, redirect, url_for, render_template
from app import create_app, login_manager
from app import auth
from app import poll_service as ps


app = create_app()

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))    
    return redirect(url_for('login'))

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
        if (auth.login(email, password)):
            return redirect(url_for("home"))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    auth.logout()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if (auth.signup(email, password)):
            if (auth.login(email, password)):
                return redirect(url_for("home"))
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route('/home')
@login_required
def home():
    polls = ps.fetch_polls()
    return render_template("custom_polls.html", user=current_user, polls=polls)

@app.route('/create_poll', methods=['GET', 'POST'])
@login_required
def create_poll():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        poll = ps.create_poll(title=title, description=description, user_id=current_user.id)
        options = [value for key, value in request.form.items() if key.startswith('option')]
        ps.create_options(options=options, poll_id=poll.id)
        
        return redirect(url_for('my_polls'))
    return render_template('create_poll.html')

@app.route('/poll/<poll_id>')
def poll(poll_id):
    if current_user.is_authenticated and ps.check_history(poll_id=poll_id, user_id=current_user.id):
        return redirect(url_for('results', poll_id=poll_id))
    poll = ps.get_poll(poll_id=poll_id)
    return render_template("poll.html", poll=poll)

@app.route("/results/<poll_id>", methods=['GET', 'POST'])
@login_required
def results(poll_id):
    if request.method == 'POST':
        selected_option_id=request.form['selected_option']
        ps.vote(user_id=current_user.id, poll_id=poll_id, option_id=selected_option_id)
    return render_template("poll_results.html", poll=ps.get_poll(poll_id=poll_id))

@app.route("/home/my_votes")
@login_required
def my_votes():
    polls = ps.get_polls_voted_by_user(user_id=current_user.id)
    return render_template("custom_polls.html", user=current_user, polls=polls)
    
    
@app.route("/home/my_polls")
@login_required
def my_polls():
    polls = ps.get_polls_created_by_user(user_id=current_user.id)
    return render_template("my_polls.html", user=current_user, polls=polls)

@app.route("/home/my_polls/delete/<poll_id>")
@login_required
def delete_poll(poll_id):
    ps.delete_poll(poll_id=poll_id)
    return redirect(url_for('my_polls'))

@app.route("/delete_account")
@login_required
def delete_account():
    auth.delete_user(user_id=current_user.id)
    return redirect(url_for('index'))

@app.route("/share/<poll_id>")
@login_required
def share_poll(poll_id):
    url = f"http://127.0.0.1:5000/poll/{poll_id}"
    qr_path="static/qr_code.png"
    qr = qrcode.make(url)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    qr_img_bytes= base64.b64encode(buffered.getvalue()).decode()
    return render_template('share_poll.html', url=url, qr_img_bytes=qr_img_bytes)