from flask import Flask, render_template, request, url_for,flash,jsonify


app = Flask(__name__)
app.secret_key = 'portfolio'




@app.route("/", methods = ["GET", "POST"])
def home():


	return render_template("index.html")


@app.route("/projects", methods = ["GET", "POST"])
def projects():


	return render_template("projects.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():


	return render_template("contact.html")





	
if __name__ == "__main__":

	app.run(debug=True) #debug = true so we do not need to re run the server anytime we make changes