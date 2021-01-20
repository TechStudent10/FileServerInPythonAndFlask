from flask import Blueprint, render_template, redirect, url_for

import os

repo = Blueprint("Repo", __name__, template_folder="templates", static_folder="static")

@repo.route("/<path:path>")
def openRepoOrUser(path):
	if path.endswith("/"):
		path = path[:len(path) - 1]

	pathList = path.split("/")
	if len(pathList) == 2:
		username = pathList[0]
		if username in os.listdir("repos"):
			repo = pathList[1]
			repos = os.path.join("repos", username)
			if repo in os.listdir(repos):
				path = os.path.join("repos", username, repo)
				files = os.listdir(path)
				return render_template('repo.html', username=username, repo_name=repo, files=files)
			else:
				return "Repository doesn't exist."
		else:
			return "User doesn't exist."
	
	if len(pathList) == 3:
		username = pathList[0]
		if username in os.listdir("repos"):
			repo = pathList[1]
			repos = os.path.join("repos", username)
			if repo in os.listdir(repos):
				filename = pathList[2]
				files = os.path.join(repos, repo)
				if filename in os.listdir(files):
					filePath = os.path.join("repos", username, repo, filename)
					file = open(filePath, "r")
					data = file.read()
					file.close()

					file = {
						'name': filename,
						'content': data
					}

					return render_template("file.html", file=file)
				else:
					return "File doesn't exist."
			else:
				return "Repository doesn't exist."
		else:
			return "User doesn't exist."
	
	return redirect(url_for('home'))