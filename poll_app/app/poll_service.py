from app import db
from app.models import Poll, Option

def create_poll(title, description, creator_id):
    poll = Poll(title=title, description=description, creator_id=creator_id)
    db.session.add(poll)
    db.session.commit()
    return poll
    
def create_option(text, poll_id):
    option = Option(text=text, poll_id=poll_id)
    db.session.add(option)
    db.session.commit()