from flask import Flask, render_template, request, flash,redirect,session,url_for,g
from forms import ContactForm,SignUpForm,SignInForm,OrderForm,ProcessBillForm
from flask.ext.mail import Message, Mail
from models import db,User,OrderDb
from app import app
import sqlite3
import json

mail = Mail()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'  


@app.route('/signup',methods=['GET','POST'])
def signup():
	form = SignUpForm()
	
	if 'rollno' in session:
		return redirect(url_for('profile')) 

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html',
				form = form
			)
		else:
			user = User(request.form['rollno'] , request.form['password'],request.form['email'],request.form['room_no'],request.form['hostel'])
			
			db.session.add(user)
			db.session.commit()
			session['rollno'] = user.rollno
			print user.rollno
			print 'Fuck this shit'
			return redirect(url_for('profile'))
	
	elif request.method == 'GET':
		return render_template('signup.html',
			form = form
		)	

@app.route('/profile')
def profile():

	form = OrderForm()
	# To view this page you need to either have session or provide the required credentials else CANNOT MOVE FURTHER 
	if 'rollno' not in session:
		return redirect(url_for('signin'))

	print 'HEY I FUCKING REACHED HERE '
	# If the 'email' key does exist, we look up the server-side user email value associated with the key using session['email'], and then query the database for a registered user with this same email address (line seven). 
	user = User.query.filter_by(rollno = session['rollno']).first()
	
	if user is None:
		return redirect(url_for('signin'))
	else:
		return render_template('profile.html',form=form)



@app.route('/signin',methods=['GET','POST'])
def signin():
	form = SignInForm()
	if 'rollno' in session:
		return redirect(url_for('profile')) 

	if request.method == 'POST':

		if form.validate() == False: 
			return render_template('signin.html',form = form)
		else:
			session['rollno'] = form.rollno.data

			return redirect(url_for('profile'))
        elif request.method == 'GET':
		return render_template('signin.html',form = form)

@app.route('/details',methods=['GET'])
def details():
	if 'rollno' in session:
		data = {}
		orders = OrderDb.query.filter_by(rollno = session['rollno']).all()
		data['rollno'] = session['rollno']
		data['order'] = [(order.order,order.status) for order in orders]
		print data
		return render_template('details.html',
				data=data)

@app.route('/confirm',methods=['GET','POST'])
def confirm():
	form = OrderForm()
	data = {}

	if 'rollno' in session:
		if request.method == 'POST':
			#Give a db query to get the "name" from the customers table 
			data['rollno'] = session['rollno']
			order = ' '.join(request.form.getlist('order'))
			data['order'] = [(order,'Requested')]

			new_order = OrderDb(data['rollno'] ,order,'Requested') # by default status=Requested
			db.session.add(new_order)
			db.session.commit()

			return render_template('details.html',
				data = data) # Make detail.html

		elif request.method =='GET':
			print 'fuck this shit'
			return render_template('profile.html',
				form=form)
	else:
		return redirect(url_for('signin'))


@app.route('/admin',methods=['GET','POST'])
def admin():
	
	form = ProcessBillForm()	
	if request.method=='GET':
		data = {} # storing all the details of the users 
		orders = OrderDb.query.filter_by(status = 'Requested').all()
		for new in orders:
			data[new.id] = [new.order,new.status]
		print data
		return render_template('admin.html',data = data,form=form)

	elif request.method == 'POST':		
		# update the OrderDb for particular id and name -> give the db Query
		ids = request.form.getlist('id')	
		print ids
		for identity in ids:
			#thanks to this fucking page : http://stackoverflow.com/questions/6699360/flask-alchemy-update-row
			rows_changed = OrderDb.query.filter_by(id=identity).update(dict(status="Seen"))
			db.session.commit()

		orders = OrderDb.query.filter_by(status = 'Requested').all()
		data = {}
		for new in orders:
			data[new.id] = [new.order,new.status]
		
		return render_template('admin.html',data = data,form=form)


@app.route('/signout')
def signout():
	if 'rollno' not in session:
		redirect(url_for('signin'))
	session.pop('rollno',None)
	return redirect(url_for('home'))
