from app import app
from flask import render_template

@app.route("/admin/")
def home():
    return render_template("pages/admin/index.html")