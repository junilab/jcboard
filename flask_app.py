from flask import Flask, request, render_template, flash, jsonify, json, session, escape


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
	return render_template("main.html")

app.run(host='202.68.230.185', debug=True)
