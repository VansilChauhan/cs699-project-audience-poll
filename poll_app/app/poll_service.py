from app import db
from app.models import Poll, Option, Vote
from sqlalchemy import func

def create_poll(title, description, creator_id):
    poll = Poll(title=title, description=description, creator_id=creator_id)
    db.session.add(poll)
    db.session.commit()
    return poll
    
def create_option(text, poll_id):
    option = Option(text=text, poll_id=poll_id)
    db.session.add(option)
    db.session.commit()
    
def fetch_polls():
    return Poll.query.all()

def get_poll(poll_id):
    return Poll.query.filter_by(id=poll_id).first()

def vote(poll_id, option_id, user_id):
    vote = Vote(user_id=user_id, poll_id=poll_id, option_id=option_id)
    # option.vote_count=option.votes.count()
    db.session.add(vote)
    db.session.commit()
    
def get_vote_counts_for_poll(option_id):
    vote_count = (
        db.session.query(func.count(Vote.id))
        .filter(Vote.option_id==option_id)
        .scalar()
    )
    return vote_count