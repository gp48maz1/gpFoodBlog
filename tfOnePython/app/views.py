from flask import render_template
from app import app
#from forms import LoginForm

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

@app.route('/italian')
def italian():
	user = { 'nickname': 'Mazzone'}
	#need to handle when user is not signed in??
	food = [
		{ 
			'style': 'Italian',
			'restaurant': 'Cafe Nonna',
			'item': 'Penne Pasta in Red Sauce'
			#Do I make an ID to reference which posts are attached to this food item?
		},
		{ 
			'style': 'Italian',
			'restaurant': 'My House',
			'item': 'Bow Tie Pasta in White Sauce'
			#Do I make an ID to reference which posts are attached to this food item?
		},		
		{ 
			'style': 'Mexican',
			'restaurant': 'Local Taco',
			'item': 'Macaroni Cheese Ball'
			#Do I make an ID to reference which posts are attached to this food item?
		}
	]
	#posts = []
	return render_template("italian.html",
		title = 'Italian',
		user = user,
		food = food)

@app.route('/mexican')
def mexican():
	return render_template("mexican.html",
		title = 'Mexican')

@app.route('/thai')
def thai():
	return render_template("thai.html",
		title = 'Thai')

@app.route('/american')
def american():
	return render_template("american.html",
		title = 'American')

@app.route('/likes')
def likes():
	return render_template("likes.html",
		title = 'Likes')

@app.route('/dislikes')
def dislikes():
	return render_template("dislikes.html",
		title = 'Dislikes')

@app.route('/troll')
def troll():
	return render_template("troll.html",
		title = 'Troll')

@app.route('/posts')
def posts():
	return render_template("posts.html",
		title = 'Posts')

@app.route('/profile')
def profile():
	return render_template("profile.html",
		title = 'Profile')


