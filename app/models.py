from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    views = db.Column(db.Integer,default=0)
    comments = db.Column(db.Integer,default=0)
    date_pub = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    

def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}', '{self.user_id}')"

class User(UserMixin,db.Model):
    __tablename_ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(200))
    username = db.Column(db.String(255))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author',lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'