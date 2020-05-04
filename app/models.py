from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'USERS'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))


    def __repr__(self):
        return f'User {self.username}'
