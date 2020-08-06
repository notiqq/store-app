from app import app

@app.route("/admin/")
def home():
    return "Hello admin!"