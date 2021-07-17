from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """renders welcome text"""
    return "welcome"

@app.route("/welcome/home")
def home():
    """renders welcome home text"""
    return f"welcome home"

@app.route("/welcome/back")
def back():
    """renders welcome back text"""
    return f"welcome back"

