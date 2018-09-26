from flask import Flask

app = Flask(__name__)


# Get homepage
@app.route("/")
@app.route("/home")
def home():
    return "Hello World!"


# About page
@app.route("/about")
def about():
    return "<h1>About page!</h1>"


if __name__ == '__main__':
    app.run(port=2000, debug=True)
