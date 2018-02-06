from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

# Pitch Model


class Pitch(db.Model):  # (db.Model)
    """
    Defining the pitch object
    """
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    author = db.Column(db.String)
    category = db.Column(db.String)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches

    @classmethod
    def get_categories(cls, category):
        pitch_cat = Pitch.query.filter_by(category=category)
        return pitch_cat

    all_pitches = []

    def __init__(self,
                 title,
                 body,
                 author,
                 category,
                 upvotes,
                 downvotes):
        self.title = title
        self.body = body
        self.author = author
        self.category = category
        self.upvotes = upvotes
        self.downvotes = downvotes
        # self.user = user


class Comment(db.Model):  # (db.Model)
    """
    Defining the pitch object
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.all()
        return comments

    all_comments = []

    def __init__(self,
                 title,
                 comment,
                 user):
        self.title = title
        self.comment = comment
        self.user = user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User Model


class User(UserMixin, db.Model):
    """
    Defining the user object
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    # pitches = db.relationship('Pitch', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Pitch {self.username}'
    # pass


# class Review(db.Model):
#     """
#     Defining the review object
#     """
#     pass
