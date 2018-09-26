from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dbbcb0b80858d417a39c0ee0d44d7d78'

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
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


# Login Route
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=2000, debug=True)
