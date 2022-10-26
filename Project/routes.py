from config import app
from flask import render_template, request, redirect, url_for

@app.route("/")
def home():
	return render_template("login.html")

@app.route('/login')
def login():
	return render_template("login.html")