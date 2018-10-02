from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Dummy data
posts = [
    {
        'author': 'Richard Tumapon',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'September 25, 2018'
    },

    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'September 26, 2018'
    }
]


# Get homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


# About page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


# Registration route
@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current user is logged in redirect to homapage
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current user is logged in redirect to homapage
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        # check if the user exists
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Logged the user in
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# Logout Route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# Account route
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
