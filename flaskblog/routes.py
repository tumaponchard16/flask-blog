from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
