from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from models import User

def load_user(user_id):
    return User.query.get(int(user_id))

# returns True if login attempt succeeds, else False
def login(email, password):
    global User
    user = User.query.filter_by(email=email).first()

    # Verify user exists and password is correct
    if user and check_password_hash(user.password, password):
        return login_user(user)
        
    return False

def logout():
    logout_user()


def signup(email, password):
    # Check if the user already exists
    global User
    user = User.query.filter_by(email=email).first()
    if user: # user already exists
        return False
    
    # TODO: verify email
    # Hash the password and create a new user
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return True