import os
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask_wtf import FlaskForm
from .forms import PostForm
from .models import User
from . import db
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask_login import login_required, current_user


auth = Blueprint('auth', __name__)

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL= True,
    MAIL_USERNAME = 'jisnderi@gmail.com',
    MAIL_PASSWORD = 'Kenyatta100@#',
))
mail = Mail(app)
mail.init_app(app)

s = URLSafeTimedSerializer('thisisasecret!')
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['GET','POST'])
def signup_post():
    email = request.form.get('email')

    msg = Message('Welcome To Pitches!', sender="jisnderi@gmail.com", recipients=[email])
    msg.body = 'Welcome To Pitches!. Thanks for creating an account, regards <br> ~ Gerald Mwanu'

    mail.send(msg)

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))


@auth.route("/createpost", methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.date, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created')
        return redirect(url_for('auth.route'))
    return render_template('create_post.html', title='New Post', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/profile')
@login_required
def profile():
    image_file = url_for('static', filename='profile_picture/' + current_user.image_file)
    return render_template('profile.html', title=profile, image_file=image_file)
