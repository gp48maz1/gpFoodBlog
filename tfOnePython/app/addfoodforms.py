from flask.ext.wtf import Form, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms import TextField, BooleanField, RadioField, IntegerField
from wtforms.validators import Required
from models import db, User

class FoodForm(Form):
	#style = IntegerField('style', validators = [Required()])
	restaurant = IntegerField('restaurant', validators = [Required()])
	dish = TextField('dish', validators = [Required()]) #Maybe also make a validator that makes in check against a list
	cat1 = IntegerField('cat1', validators = [Required()])
	cat2 = IntegerField('cat2', validators = [Required()])

class Category1Form(Form):
	category1 = TextField('category1', validators = [Required()])

class Category2Form(Form):
	category2 = TextField('category2', validators = [Required()])

class StyleForm(Form):
	style = TextField('style', validators = [Required()])

class RestaurantForm(Form):
	style = IntegerField('style', validators = [Required()])
	restaurant = TextField('restaurant', validators = [Required()])

class SignupForm(Form):
	firstname = TextField("First name", [validators.Required("Please enter your first name.")])
	lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create account")

	#I wasnt using constructors before....
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True

#class ResturantForm(Form):
#	style = DropDown('style', validators = [Required()])
#	resturant = TextField('resturant', validators = [Required()])

#HOW TO ADD RADIO BUTTONS
#	cat2 = RadioField('cat2',
#		choices = [('Any','Any'),
#		('None', 'None'),
#		('Chicken', 'Chicken'),
#		('Beef', 'Beef'),
#		('Pork', 'Pork')])
#