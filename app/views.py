from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("pages/public/index.html")


@app.route("/about")
def about():
    return "something"
