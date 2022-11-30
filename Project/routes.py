from config import app
from flask import render_template, request, redirect, url_for

@app.route("/")
def home():
	try:
		print(session, flush=True)
		if session['loggedin'] != None:
			if session['HR'] == 1:
				return render_template('hr_dashboard.html')
			else:
				return render_template('dashboard.html')
		else:
			return redirect(url_for('login'))
	except Exception as e:
		print(e)
		return redirect(url_for('login'))
		
@app.route('/login')
def login():
	return render_template("login.html")