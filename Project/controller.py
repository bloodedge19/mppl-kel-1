from config import *
from flask import render_template, request, redirect, url_for, session
from werkzeug.datastructures import ImmutableMultiDict
import MySQLdb.cursors
import db
import re

@app.route('/login', methods =['GET', 'POST'])
def do_login():
	mysql = db.connect()
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM employees where email = %s', (email, ))
		rv = cursor.fetchone()
		print(rv, flush=True)
		if bcrypt.check_password_hash(rv['password'], password):
			session['loggedin'] = True
			session['id'] = rv['employee_id']
			session['fullname'] = rv['fullname']
			session['HR'] = rv['isHR']
			msg = 'Logged in successfully !'
			cursor.close()
			mysql.close()
			return render_template("index.html", msg = msg)
		else:
			cursor.close()
			mysql.close()
			msg = 'Incorrect email / password !'
	return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	mysql = db.connect()
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		data = request.form.to_dict()
		password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
		cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM employees WHERE email = %s', (data['email'], ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', data['email']):
			msg = 'Invalid email address !'
		elif not data['password'] or not data['email']:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO employees VALUES (NULL, %s, %s, %s, %s, 0)', (data['email'], password, data['fullname'], data['salary'], ))
			mysql.commit()
			msg = 'You have successfully registered !'
			cursor.close()
			mysql.close()
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
		cursor.close()
		mysql.close()
	return render_template('register.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('fullname', None)
	return redirect(url_for('login'))
