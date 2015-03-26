from MoviesApp import db

class Movies(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), unique=True)
	poster = db.Column(db.String(255), unique=True)
	year = db.Column(db.Integer)

	def __init__(self, id, title, poster, year):
		self.id = id
		self.title = title
		self.poster = poster
		self.year = year

class Wishlists(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	items = db.relationship('WishlistItems', backref='wishlist', lazy='dynamic')

	def __init__(self, id, user_id):
		self.id = id
		self.user_id = user_id

class WishlistItems(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlists.id'))
	movie_id = db.Column(db.Integer)

	def __init__(self, id, wishlist_id, movie_id):
		self.id = id
		self.wishlist_id = wishlist_id
		self.movie_id = movie_id

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	device_token = db.Column(db.String(255),unique=True)

	def __init__(self, device_token):
		self.device_token = device_token
