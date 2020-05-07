from flask import Blueprint, render_template 
from flask_login import login_required, current_user
from .models import Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)