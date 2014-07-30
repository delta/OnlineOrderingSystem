from werkzeug import generate_password_hash, check_password_hash 
from app import db

#Order Db for admin to query and update status once seen 
class OrderDb(db.Model):
	__tablename__ = 'new_orders'
	id  = db.Column(db.Integer,primary_key=True) # uniquely identify an order(autoincrement)
	rollno = db.Column(db.Integer)
	order = db.Column(db.String(200))
	status = db.Column(db.String(50))		

	def __init__(self,rollno,order,status):
		self.rollno = rollno
		self.order = order.title()
		self.status = status.title()
	
	def get_id(self):
		return unicode(self.id)
	
class User(db.Model):
	__tablename__ = 'customers'
	uid =  db.Column(db.Integer, primary_key = True)
	rollno = db.Column(db.Integer)
	room_no = db.Column(db.Integer)
	hostel=db.Column(db.String(100))
	email=db.Column(db.String(100),unique = True)
	pwdhash=db.Column(db.String(54))
	
	def __init__(self, rollno,password,email,room_no,hostel):
    		self.rollno = rollno
        	self.room_no = room_no
		self.hostel = hostel.title()
		self.email = email.lower()
		self.set_password(password)

	def set_password(self, password):
	    self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
	    return check_password_hash(self.pwdhash, password)

	def is_authenticated(self):
		return True
	

	def is_active(self):
		return True

	def is_anonymous(self):
		return False
	
	def get_id(self):
		return unicode(self.id)
	
	def __repr__(self):
		return '<User %r>' % (self.rollno)
