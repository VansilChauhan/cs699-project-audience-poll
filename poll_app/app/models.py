from app import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


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
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), unique=True, nullable=False) # store the hash password
    is_admin = db.Column(db.Boolean, default=False)
    
    polls = db.relationship('Poll', backref='creator', lazy=True, cascade="all, delete-orphan")
    votes = db.relationship('Vote', backref='voter', lazy=True)
    vote_history = db.relationship('UserVoteHistory', backref='user', lazy=True)

class Poll(db.Model):
    __tablename__ = 'poll'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at =db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(20), default='active')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    options = db.relationship('Option', backref='poll', lazy=True)
    votes = db.relationship('Vote', backref='poll', lazy=True)
    vote_history = db.relationship('UserVoteHistory', backref='poll', lazy=True)
    
    @hybrid_property
    def vote_count(self):
        return len(self.votes)
    
    @hybrid_property
    def created_by_username(self):
        creator = User.query.get(self.creator_id)
        name, _, _ =creator.email.rpartition('@')
        return name
    
class Option(db.Model):
    __tablename__ = 'option'
    id= db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    # vote_count = db.Column(db.Integer, default=0)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    
    votes = db.relationship('Vote', backref='option', lazy=True)
    
    @hybrid_property
    def vote_count(self):
        return len(self.votes)
    
class Vote(db.Model):
    __tablename__ = 'vote'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
    voted_at = db.Column(db.DateTime, default=datetime.now)

class UserVoteHistory(db.Model):
    __tablename__ = 'user_vote_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'),nullable=False)
    vote_submitted = db.Column(db.Boolean, default=True)