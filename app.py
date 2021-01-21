from flask import Flask, render_template
from repo import repo
from user import user

app = Flask(__name__)
app.register_blueprint(repo)
app.register_blueprint(user, url_prefix="/user")

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)