# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.marshmallow import Marshmallow

app = Flask(__name__)

with app.app_context():
	api = restful.Api(app)

	app.config.from_envvar('MOVIESAPP_SETTINGS')
	
	db = SQLAlchemy(app)

	ma = Marshmallow(app)

	##### MODELS #####

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

	##### SCHEMAS #####

	class MovieSchema(ma.Schema):
	    class Meta:
	        # Fields to expose
	        fields = ('id', 'title', 'poster','year')

	movie_schema = MovieSchema(many=True)

	##### API #####

	class Discover(restful.Resource):
	    def get(self):
	    	movies = Movies.query.filter(Movies.poster != None).filter(Movies.year <= 2015).order_by(Movies.year.desc()).limit(5000).all()
	    	result = movie_schema.dump(movies)
	        return jsonify({"movies":result.data})

	api.add_resource(Discover, '/v1/discover')

	if __name__ == '__main__':
	    app.run(debug=True)
