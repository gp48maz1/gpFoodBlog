from . import db #I got this from the __init__ but why can i feed in SQLAlchemy(app)
# use . cause already in app folder
#from sqlalchemy import Column, Integer, Foreign Key, create_engine, String -- I assume I dont need cause of the above?
#from sqlalchemy.orm import relationship, sessionmaker --Needed? cause of app?

#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base() -- Are these two lines not needed cause were using db.Model vs Base?

ROLE_USER = 0
ROLE_ADMIN = 1

STYLE_ITALIAN = 0
STYLE_MEXICAN = 1
STYLE_AMERICAN = 2
STYLE_THAI = 3

REST_CAFENONNA = 0
REST_MYHOUSE = 1
REST_WHISKEYKITCHEN = 2


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index = True, unique = True) #why index?
	email = db.Column(db.String(120), index = True, unique = True) #why index?
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic') #lazy dynamic?; backref author?
	foods = db.relationship("Food", backref = 'User') #need db.?

	#what is this line
	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % (self.body)

class Food(db.Model):
	# is it good to put __tablename__ = 'food' ?? is that standard SQL alchemy practice?
	id = db.Column(db.Integer, primary_key = True)
	item = db.Column(db.String(140))
	restaurant_ID = db.Column(db.SmallInteger, db.ForeignKey('restaurant.id') ) #Should use Foreign key?
	category1_ID = db.Column(db.SmallInteger, db.ForeignKey('category1.id')) #changed to id
	category2_ID = db.Column(db.SmallInteger, db.ForeignKey('category2.id'))
	userID_entered = db.Column(db.SmallInteger, db.ForeignKey('user.id')) #this would be 1to1, or how does this work... this is only eneterd so its still foreign key, 1 user can enter many
	timestamp = db.Column(db.DateTime)
		#'date_entered': '09-09-2014',
		#'userID_entered': '1000', 
		#'style': 'Italian',
		#'restaurant': 'Cafe Nonna',
		#'category1': 'Pasta', #Category 1 is the dish cateogry
		#'category2': 'Any', #Category 2 is the type of meat
		#'item': 'Penne Pasta in Red Sauce'

class Category2(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	foods = db.relationship("Food", backref = 'Category2')

class Category1(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	foods = db.relationship("Food", backref = 'Category1') #is the backref author or self? and lazy dynainc??

class Restaurant(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	style_ID = db.Column(db.SmallInteger, db.ForeignKey('style.id'))
	name = db.Column(db.String(140))
	foods = db.relationship('Food', backref = 'Restaurant', lazy = 'dynamic') #This is for shortcut

class Style(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	restaurants = db.relationship('Restaurant', backref = 'Style', lazy = 'dynamic')

#this is what is used to create an instance of the db? line by line what does this do?
#engine = create_engine('sqlite:///:memory:', echo = True)
#Session = sessionmaker(bind = engine)
#db_session = Session()

#db.Model.metadata.create_all(engine) #changed Base to db.model

#what is the backref and uselist?