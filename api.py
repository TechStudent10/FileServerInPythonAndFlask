from flask import Blueprint, request, url_for

import os

api = Blueprint("API", __name__)

@api.route("/user/signup")
def signupUser():
	username = request.form.get('username')
	password = request.form.get('password')

	users = os.listdir("repos")
	if username not in users:
		os.mkdir(os.path.join("repos", username))

		return redirect(url_for('openRepoOrPath', path=username))