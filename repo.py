from flask import Blueprint, render_template

import os

repo = Blueprint("Repo", __name__, template_folder="templates", static_folder="static")

@repo.route("/<username>/<repo>")
def openRepo(username, repo):
	if username in os.listdir("repos"):
		if repo in os.listdir(os.path.join("repos", username)):
			path = os.path.join("repos", username, repo)
			files = os.listdir(path)

			return render_template("repo.html", username=username, repo_name=repo, files=files)

		return "Repository doesn't exist."

	return "User doesn't exist."