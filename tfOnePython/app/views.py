from flask import render_template
from app import app
from addfoodforms import AddForm

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
	styles = [
		{'name': 'Italian'},
		{'name': 'Mexican'},
		{'name': 'Thai'},
		{'name': 'American'}
		]
	return render_template("styles.html",
		title = 'Styles',
		user = user,
		styles = styles)	

@app.route('/styles/italian')
def italian():
	#need to handle when user is not signed in??
	#posts = []
	return render_template("italian.html",
		title = 'Italian',
		user = user,
		foods = foods)

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

@app.route('/addfood')
def profile():
	form = AddForm()
	return render_template("addfood.html",
		title = 'Add Food',
		user = user,
		foods = foods,
		form = form)


