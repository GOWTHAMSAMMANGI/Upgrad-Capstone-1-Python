from flask import Flask

app = Flask(__name__)

@app.route("/")
def my_world():
    return "<p>Welcome to he Python World!!!See the Miracles!!</p>"
