from email_validator import validate_email, EmailNotValidError
from flask import Flask, render_template, request, redirect, url_for, flash

# import logging

# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "flaskapp123456789"
# app.logger.setLevel(logging.DEBUG)
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# toolbar = DebugToolbarExtension(app)


@app.route("/")
def index():
    return "Hello, Flask Minimal App!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("Username is required.")
            is_valid = False

        if not email:
            flash("Email address is required.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Enter correct email style.")
            is_valid = False

        if not description:
            flash("Description is required.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        flash("Email with your description is sending. Thank you.")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
