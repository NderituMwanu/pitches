# from flask import render_template
# from app import auth

# @auth.route('/login')
# def login():
#     return render_template('auth/login.html')

# import os
# from flask import render_template, url_for,redirect,flash,request
# from app.forms import PostForm

# @app.route("/post/new", methods=['GET','POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         flash('Your post has been created')
#         return redirect(url_for('home')
#     return render_template('create_post.html', title='New Post', form =form)

