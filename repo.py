from flask import Blueprint, render_template, redirect, url_for
from pathlib import Path

import os

repo = Blueprint("Repo", __name__, template_folder="templates", static_folder="static")

@repo.route("/<path:path>")
def openRepoOrUser(path):
	# Check if / is at the end of path and handle it.
	if path.endswith("/"):
		# Path equals the path without the last letter ("/").
		path = path[:len(path) - 1]

	# Split the path into a list
	pathList = path.split("/")

	if len(pathList) == 1:
		user = pathList[0]
		if user in os.listdir('repos'):
			return "User page."
		else:
			return "User doesn't exist."

	if len(pathList) >= 2:
		path = ""
		count = 0
		for p in pathList:
			count += 1
			if count == 1:
				path = p
			else:
				path = os.path.join(path, p)

		pathVar = Path(path)

		if pathVar.is_dir():
			return render_template("repo.html", files=os.listdir(path))
		else:
			file = open(path, "r")
			data = file.read()
			file.close()
			return render_template("file.html", file={"name": os.basename(path), "content": data})
	
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