from flask import render_template, redirect, url_for, request
from app import app
from addfoodforms import AddForm, StyleForm, RestaurantForm
from models import db, Food, Style, Restaurant #where did the database we created last time go?

user = { 'nickname': 'Mazzone'}

foods = [
	{
		'ID': '0',
		'date_entered': '09-09-2014',
		'userID_entered': '1000', 
		'style': 'Italian',
		'restaurant': 'Cafe Nonna',
		'category1': 'Pasta', #Category 1 is the dish cateogry
		'category2': 'Any', #Category 2 is the type of meat
		'item': 'Penne Pasta in Red Sauce'
		#rating which will be a calculated field -- an average of all ratings posted!@!@#$!#@$!@#%
		#Do I make an ID to reference which posts are attached to this food item?
	},
	{ 
		'ID': '1',
		'date_entered': '09-09-2014',
		'userID_entered': '1001', 
		'style': 'Italian',
		'restaurant': 'My House',
		'category1': 'Pasta',
		'category2': 'Any',
		'item': 'Bow Tie Pasta in White Sauce'
		#Do I make an ID to reference which posts are attached to this food item?
	},		
	{
		'ID': '2',
		'date_entered': '09-09-2014',
		'userID_entered': '1000',  
		'style': 'Mexican',
		'restaurant': 'Local Taco',
		'category1': 'Pasta',
		'category2': 'None',
		'item': 'Macaroni Cheese Ball'
		#Do I make an ID to reference which posts are attached to this food item?
	},
	{
		'ID': '3',
		'date_entered': '09-11-2014',
		'userID_entered': '1001',  
		'style': 'American',
		'restaurant': 'Whiskey Kitchen',
		'category1': 'Sandwhich',
		'category2': 'Beef',
		'item': 'Flank Steak Sandwhich'
		#Do I make an ID to reference which posts are attached to this food item?
	},
	{
		'ID': '4',
		'date_entered': '09-11-2014',
		'userID_entered': '1002',  
		'style': 'Thai',
		'restaurant': 'Smiling Elephant',
		'category1': 'Pasta',
		'category2': 'Any',
		'item': 'Pad Thai'
		#Do I make an ID to reference which posts are attached to this food item?
	}
]

posts = [
	{
		'ID': '0',
		'date_entered': '09-09-2014',
		'userID_entered': '1000',
		'foodID': '0',
		'foodPost': 'I love red sauce so much more than white saue!',
		'like': 'True', #make condition so that only not both like and dislike active -- but can have neither
		'dislike': 'False',
		'troll': 'False',
		'rating': '9' #scale of 1-10
		#If I want users to be able to like or dislike this comment do I need to make fields for that?
	}
]

restaurants = [li['restaurant'] for li in foods] #Find a way to keep the Style so can list in html 

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Mazzone'}
	#need to handle when user is not signed in??
	return render_template("index.html",
		title = 'Home',
		user = user
		)
		#posts = posts
		#)

@app.route('/about')
def about():
	return render_template("about.html",
		title = 'About')

@app.route('/styles')
def styles():
	styles = Style.query.all()
		#[
		#{'name': 'Italian'},
		#{'name': 'Mexican'},
		#{'name': 'Thai'},
		#{'name': 'American'}
		#]
	return render_template("styles.html",
		title = 'Styles',
		user = user,
		styles = styles)

@app.route('/styles')
def styles():
	styles = Style.query.all(),
	restaurants = Restaurant.query.all()
	return render_template("styles.html",
		title = 'Styles',
		user = user,
		styles = styles, 
		restaurants = restaurants)	

@app.route('/styles/italian')
def italian():
	#need to handle when user is not signed in??
	#posts = []
	return render_template("italian.html",
		title = 'Italian',
		user = user,
		foods = foods,
		restaurants = restaurants)

@app.route('/styles/mexican')
def mexican():
	return render_template("mexican.html",
		title = 'Mexican',
		user = user,
		foods = foods)

@app.route('/styles/thai')
def thai():
	return render_template("thai.html",
		title = 'Thai',
		user = user,
		foods = foods)

@app.route('/styles/american')
def american():
	return render_template("american.html",
		title = 'American',
		user = user,
		foods = foods)

@app.route('/profile/likes')
def likes():
	return render_template("likes.html",
		title = 'Likes')

@app.route('/profile/dislikes')
def dislikes():
	return render_template("dislikes.html",
		title = 'Dislikes')

@app.route('/profile/troll')
def troll():
	return render_template("troll.html",
		title = 'Troll')

@app.route('/profile/posts')
def posts():
	return render_template("posts.html",
		title = 'Posts')

@app.route('/profile')
def profile():
	return render_template("profile.html",
		title = 'Profile')

@app.route('/addstyle', methods = ["GET"])
def addstyle_get():
	form = StyleForm()
	return render_template("addstyle.html",
		title = 'Add Style',
		user = user,
		form = form)

@app.route('/addstyle', methods = ["POST"])
def addstyle_post():
	form = StyleForm()
	style =  Style(
		name = request.form["style"]
		)
	db.session.add(style)
	db.session.commit()
	return redirect(url_for("index"))

@app.route('/addrestaurant', methods = ["GET"])
def addrestaurant_get():
	form = RestaurantForm(),
	styles = Style.query.all()
	return render_template("addrestaurant.html",
		title = 'Add Restaurant',
		styles = styles,
		user = user,
		form = form)

@app.route('/addrestaurant', methods = ["POST"])
def addrestaurant_post():
	form = RestaurantForm()
	restaurant =  Restaurant(
		style_id = request.form["style"],
		name = request.form["restaurant"]
		)
	db.session.add(restaurant)
	db.session.commit()
	return redirect(url_for("index"))

#am i supposed to add in a post AND a get route???
#if i dont include POST or GET does it just default use on both? i.e. no method = ... it will use this for post of get or will say i need post even if it works for post
@app.route('/addfood', methods = ["GET"])
#have to parse form on view 
def addfood_get():
	form = AddForm() # do i need this line here if I am seperating GET and POST? Also can i put them in the same route and seperate with an if?
	return render_template("addfood.html",
		title = 'Add Food',
		user = user,
		foods = foods,
		form = form)

@app.route('/addfood', methods = ["POST"])
def addfood_post():
	form = AddForm()
	food = Food(
		style = request.form["style"], # needs to be a drop down from available 
		resturant = request.form["resturant"], # drop down from available
		item = request.form["dish"],
		cat1 = request.form["cat1"], #does this work when using radio buttons
		cat2 = request.form["cat2"] #does this work when using radio buttons
		)
	session.add(food)
	session.commit()
	return redirect(url_for("index")) #is this how you use this?


