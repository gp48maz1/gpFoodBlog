from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, RadioField
from wtforms.validators import Required

class AddForm(Form):
	style = TextField('style', validators = [Required()])
	resturant = TextField('resturant', validators = [Required()])
	dish = TextField('dish', validators = [Required()]) #Maybe also make a validator that makes in check against a list
	cat1 = RadioField( 'cat1', 
		choices = [('Pasta', 'Pasta'),
		('Sandwhich', 'Sandwhich'),
		('Dessert', 'Dessert'),
		('Entree', 'Entree') ])
	cat2 = RadioField('cat2',
		choices = [('Any','Any'),
		('None', 'None'),
		('Chicken', 'Chicken'),
		('Beef', 'Beef'),
		('Pork', 'Pork')])
