from flask import Blueprint, render_template

user = Blueprint("user", __name__, template_folder="templates", static_folder="static")

@user.route("/login")
def login():
	return render_template("login.html")

@user.route("/signup")
def signup():
	return render_template("signup.html")