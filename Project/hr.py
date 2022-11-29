from config import *
from flask import render_template, request, redirect, url_for, session, abort
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
import time

def calculate(emp_id):
	try:
		standard = 0
		mysql = db.connect()
		cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
		now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
		today = now.strftime("%Y-%m-%d")
		cursor.execute("SELECT working_hours FROM log_employees where employee_id = %s and clock_in >= %s", (emp_id, today, ))
		rv = cursor.fetchone()
		print(rv['working_hours'], flush=True)
		sec = time.strptime(str(rv['working_hours']), "%H:%M:%S")
		sec = int(datetime.timedelta(hours=sec.tm_hour,minutes=sec.tm_min,seconds=sec.tm_sec).total_seconds())
		if(sec - standard > 0):
			res = sec - standard
			ovt_salary = int(((res/sec) / 100) * 12000000)
			print(res, ovt_salary, flush=True)
			cursor.execute("UPDATE employees SET overtime_salary = SUM(overtime_salary+%s) where employee_id = %s", (ovt_salary, emp_id, ))
			mysql.commit()
			cursor.close()
			mysql.close()
			return
		else:
			cursor.close()
			mysql.close()
			return
	except Exception as e:
		print(e)
		return



@app.route("/payroll")
def payroll():
	try:
		if(session['HR'] == 1):
			return render_template("hr_payroll.html")
		else:
			return "Not HR"
	except:
		return redirect(url_for('dashboard'))


@app.route("/get_payroll")
def get_payroll():
	try:
		if(session['HR'] == 1):
			#select payroll_id, payroll.employee_id, employees.fullname, employees.salary, payroll.status FROM payroll INNER JOIN employees ON payroll.employee_id=employees.employee_id;
			mysql = db.connect()
			cursor = mysql.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute("select payroll_id, payroll.employee_id, employees.fullname, employees.salary, employees.overtime_salary, payroll.status FROM payroll INNER JOIN employees ON payroll.employee_id=employees.employee_id")
			row_headers=[x[0] for x in cursor.description]
			rv = cursor.fetchall()
			print(rv, flush=True)
			json_data = []
			for i in range(len(rv)):
				data = {}
				data['employee_id'] = (rv[i]['employee_id'])
				data['fullname'] = (rv[i]['fullname'])
				data['salary'] = (rv[i]['salary'])
				data['overtime_salary'] = (rv[i]['overtime_salary'])
				data['total_salary'] = int(data['salary']) + int(data['overtime_salary'])
				data['status'] = (rv[i]['status'])
				json_data.append(data)
			cursor.close()
			mysql.close()
			return json.dumps(json_data, default=str)
		else:
			return "Not HR"
	except:
		return redirect(url_for('dashboard'))
