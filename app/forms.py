from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError,PasswordField,SelectMultipleField
from models import db,User

class ContactForm(Form):
  rollno = TextField("RollNo",  [validators.Required("Please enter your Roll.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")

class ProcessBillForm(Form):
	ids = SelectMultipleField("id",choices=[])
	submit = SubmitField("Send")

class OrderForm(Form):
	
	order = SelectMultipleField("order",choices=[])
	submit = SubmitField("Send")

class SignUpForm(Form):
	rollno = TextField("RollNo ",  [validators.Required("Please enter your Roll Number.")])
	room_no = TextField("Room No",  [validators.Required("Please enter your last name.")])
	hostel = TextField("Hostel ",  [validators.Required("Please enter your last name.")])
  	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  	password = PasswordField('Password', [validators.Required("Please enter a password.")])
  	submit = SubmitField("Create account")

	def __init__(self,*args,**kwargs):
		Form.__init__(self, *args, **kwargs)
	
	def validate(self):
		if not Form.validate(self):
			return False
		#if the form is filled properly or not 
		user = User.query.filter_by(email=self.rollno.data).first()
		if user:
			return False; 
			# Fucker  already exists
		else:
			return True

#class AdminForm(Form):

#	username = TextField("Username",  [validators.Required("Please enter your Username.")])
# 	password = PasswordField('Password', [validators.Required("Please enter a password.")])
#  	submit = SubmitField("Create account")

#	def __init__(self,*args,**kwargs):
#		Form.__init__(self, *args, **kwargs)
	
#	def validate(self):
#		if not Form.validate(self):
#			return False
#		#if the form is filled properly or not 
#		if self.username=='ADMIN' and self.password='because-i-can':
#			return True
#		else:
#			return False
		
class SignInForm(Form):
	
	rollno = TextField("rollno",  [validators.Required("Please enter your rollno.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Sign In")
	
	def __init__(self, *args, **kwargs):
	    Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(rollno = self.rollno.data).first()
		if user and user.check_password(self.password.data):
			return True
		else:
			#invalid username-password
			return False
