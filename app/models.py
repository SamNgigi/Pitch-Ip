from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Pitch(db.Model):  # (db.Model)
    """
    Defining the pitch object
    """
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    all_pitches = []

    def __init__(self, id, title, body, author, category, upvotes, downvotes):
        self.id = id
        self.title = title
        self.body = body
        self.author = author
        self.category = category
        self.upvotes = upvotes
        self.downvotes = downvotes


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    Defining the user object
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    pass


# class Review(db.Model):
#     """
#     Defining the review object
#     """
#     pass
