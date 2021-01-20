from flask import Blueprint, render_template, redirect, url_for

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
	# If the length of the path is equal to two and handle it.
	if len(pathList) == 2:
		# Username is the first object in pathList
		username = pathList[0]
		# If the username is in the repos folder and handle it.
		if username in os.listdir("repos"):
			# Repo is the second object in pathList
			repo = pathList[1]
			# Repos is a list of all the repos/the username defined above.
			repos = os.path.join("repos", username)
			# If the repo is in the repos/the username defined above and handle it.
			if repo in os.listdir(repos):
				# Path is a list of repos/the username defined above/the repo defined above.
				path = os.path.join("repos", username, repo)
				# Files is a list of the path above
				files = os.listdir(path)
				# Render the repo.html template with username=username, repo_name=repo and files=files
				return render_template('repo.html', username=username, repo_name=repo, files=files)
			else:
				# Return this message if the repository doesn't exist.
				return "Repository doesn't exist."
		else:
			# Return this message if the user doesn't exist.
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