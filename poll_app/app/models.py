from app import db
from flask_login import UserMixin


'''
Flask-login requires a User model with the following properties:

    has an is_authenticated() method that returns True if the user has provided valid credentials
    has an is_active() method that returns True if the user's account is active
    has an is_anonymous() method that returns True if the current user is an anonymous user
    has a get_id() method which, given a User instance, returns the unique ID for that object

UserMixin class provides the implementation of this properties. 
Its the reason you can call for example is_authenticated to check if login credentials provide is correct or not instead of having to write a method to do that yourself.
'''

# email and password shouldn't be greater than 500 characters
# otherwise a malicious user may try to fill up our server space by putting arbitrary large strings
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), unique=True, nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False) # store the hash password