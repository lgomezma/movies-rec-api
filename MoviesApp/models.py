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