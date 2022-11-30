from config import *
from hr import *
from flask import render_template, request, redirect, url_for, session, abort, flash
from flask_login import login_required
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename
import MySQLdb.cursors
import db
import re
import datetime
import pytz
import json
import os

app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'static/uploads'

def clock_checker(emp_id, choice):
	mysql = db.connect()
	cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
	now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
	start = now.strftime("%Y-%m-%d 00:00:00")
	end = now.strftime("%Y-%m-%d 23:59:59")
	cursor.execute("SELECT log_id, clock_in, clock_out from log_employees where employee_id = %s and clock_in >= %s and clock_in < %s", (emp_id, start, end, ))
	rv = cursor.fetchone()
	if(choice == 'clock-in'):
		if (rv == None):
			return True
		elif (rv['clock_in'] is None):
			return True
		else:
			return False
	else:
		if (rv['clock_out'] is None):
			return True
		else:
			return False

@app.route('/login', methods =['GET', 'POST'])
def do_login():
	err = "Incorrect email or password"
	try:
		mysql = db.connect()
		msg = ''
		if request.method == 'POST':
			email = request.form['email']
			password = request.form['password']
			cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM employees where email = %s', (email, ))
			rv = cursor.fetchone()

			print(rv, flush=True)
			print(bcrypt.check_password_hash(rv['password'], password))
			if bcrypt.check_password_hash(rv['password'], password):
				session['loggedin'] = True
				session['id'] = rv['employee_id']
				session['fullname'] = rv['fullname']
				session['HR'] = rv['isHR']
				msg = 'Logged in successfully !'
				cursor.close()
				mysql.close()
				return redirect(url_for('dashboard'))

			else:
				cursor.close()
				mysql.close()
				flash(err)
				return redirect(url_for('login'))
		else:
			try:
				print(session['loggedin'])
				if(session['loggedin'] == True):
					return redirect(url_for('dashboard'))
				else:
					return render_template('login_html')
			except:
				return render_template('login.html')
	except Exception as e:
		print(e, flush=True)
		flash(err)
		return redirect(url_for('login'))



@app.route("/clock-in")
def clock_in():
	err = "You're already clock-in!"
	msg = "Success clock-in!"
	try:
		if(session['loggedin'] != None):
			if(clock_checker(session['id'], 'clock-in') == False):
				flash(err)
				print(err, flush=True)
				return redirect(url_for('attendance'))
			mysql = db.connect()
			print("Sesssion: ", session['id'], flush=True)
			now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
			time = now.strftime("%Y-%m-%d %H:%M:%S")
			cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('INSERT INTO log_employees VALUES (NULL, %s, %s, NULL, NULL, NULL)', (session['id'], time, ))
			mysql.commit()
			cursor.close()
			mysql.close()
			flash(msg)
			return redirect(url_for('attendance'))
	except Exception as e: 
		print(e, flush=True)
		return redirect(url_for('attendance'))

@app.route("/clock-out")
def clock_out():
	err = "You're already clock-out!"
	msg = "Success clock-out!"
	try:
		if(session['loggedin'] != None):
			check = clock_checker(session['id'], 'clock-out')
			if(check == False):
				flash(err)
				print(err, flush=True)
				return redirect(url_for('attendance'))
			mysql = db.connect()
			now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
			time = now.strftime("%Y-%m-%d %H:%M:%S")
			today = now.strftime("%Y-%m-%d")
			cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute("SELECT log_id from log_employees where employee_id = %s and clock_in >= %s", (session['id'], today))
			rv = cursor.fetchone()
			print(rv, flush=True)
			cursor.execute('UPDATE log_employees SET clock_out = %s, working_hours = TIMEDIFF(%s, clock_in) where log_id = %s', (time, time, rv['log_id']))
			mysql.commit()
			calculate(session['id'])
			cursor.close()
			mysql.close()
			flash(msg)
			return redirect(url_for('attendance'))
	except Exception as e: 
		print(e, flush=True)
		return redirect(url_for('attendance'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
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

@app.route("/attendance")
def attendance():
	try:
		if session['loggedin'] != None:
			return render_template('attendance.html')
		else:
			return redirect(url_for('login'))
	except Exception as e:
		print(e)
		return redirect(url_for('login'))

@app.route('/overtime', methods =['GET', 'POST'])
def overtime():
	try:
		if (request.method == 'GET'): 
			if session['loggedin'] != None:
				return render_template('overtime.html')
			else:
				return redirect(url_for('login'))		
			
		else:
			return redirect(url_for('dashboard'))
	except Exception as e:
		print(e)
		return redirect(url_for('dashboard'))

@app.route('/api-overtime')
def overtime_api():
	print(session, flush=True)
	if (session['loggedin'] != None):
		mysql = db.connect()
		cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
		now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
		start = now.strftime("%Y-%m-%d 00:00:00")
		end = now.strftime("%Y-%m-%d 23:59:59")
		cursor.execute("SELECT log_id, clock_in, clock_out, working_hours from log_employees where employee_id = %s", (session['id'], ))
		row_headers=[x[0] for x in cursor.description]
		rv = cursor.fetchall()
		print(rv, flush=True)
		json_data = []
		for i in range(len(rv)):
			data = {}
			data['date'] = (rv[i]['clock_in']).strftime('%m/%d/%Y')
			data['start'] = (rv[i]['clock_in']).strftime('%H:%M')
			if(rv[i]['clock_out'] == None):
				data['end'] = "--:--"
			else:
				data['end'] = (rv[i]['clock_out']).strftime('%H:%M')
				data['working_hours'] = rv[i]['working_hours']
			json_data.append(data)
		cursor.close()
		mysql.close()
		return json.dumps(json_data, default=str)

@app.route("/api-users")
def users_api():
	mysql = db.connect()
	cur = mysql.cursor()
	cur.execute("SELECT email, address, phone_number, fullname, salary, overtime_salary from employees where employee_id = %s", (session['id'], ))
	row_headers=[x[0] for x in cur.description] #this will extract row headers
	rv = cur.fetchall()
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	return json.dumps(json_data[0])
	#return "Test"

@app.route("/reimbursement", methods =['GET', 'POST'])
def reimbursement():
	try:
		if (request.method == 'GET'): 
			if session['loggedin'] != None:
				return render_template('reimbursement.html')
			else:
				return redirect(url_for('login'))
		elif (request.method == 'POST'):
			print(request.form, flush=True)
			uploaded_file = request.files['file']
			filename = secure_filename(uploaded_file.filename)
			if filename != '':
				mysql = db.connect()
				cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
				file_ext = os.path.splitext(filename)[1]
				if file_ext not in app.config['UPLOAD_EXTENSIONS']:
					return "Wrong Format"
				now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
				date = now.strftime("%Y-%m-%d")
				types = request.form['condition']
				amount = int(request.form['amount'])
				description = request.form['description']
				cursor.execute('INSERT INTO reimbursement VALUES (NULL, %s, %s, %s, %s, %s, NULL)', (session['id'], date, types, amount, description))
				mysql.commit()
				cursor.close()
				mysql.close()
				uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			return "Success"
	except Exception as e:
		print(e)
		return redirect(url_for('login'))

@app.route("/permit", methods =['GET', 'POST'])
def permit():
	try:
		if (request.method == 'GET'): 
			if session['loggedin'] != None:
				return render_template('permit.html')
			else:
				return redirect(url_for('login'))
		elif (request.method == 'POST'):
			print(request.form, flush=True)
			uploaded_file = request.files['file']
			filename = secure_filename(uploaded_file.filename)
			if filename != '':
				mysql = db.connect()
				cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
				file_ext = os.path.splitext(filename)[1]
				if file_ext not in app.config['UPLOAD_EXTENSIONS']:
					return "Wrong Format"
				now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
				date = now.strftime("%Y-%m-%d")
				types = request.form['condition']
				amount = int(request.form['amount'])
				description = request.form['description']
				cursor.execute('INSERT INTO reimbursement VALUES (NULL, %s, %s, %s, %s, %s, NULL)', (session['id'], date, types, amount, description))
				mysql.commit()
				cursor.close()
				mysql.close()
				uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
			return "Success"
	except Exception as e:
		print(e)
		return redirect(url_for('login'))