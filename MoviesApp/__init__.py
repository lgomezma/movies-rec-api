# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
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

	from MoviesApp import models

	Movies = models.Movies
	Users = models.Users

	##### SCHEMAS #####

	class MovieSchema(ma.Schema):
	    class Meta:
	        # Fields to expose
	        fields = ('id', 'title', 'poster','year')

	movie_schema = MovieSchema(many=True)

	##### API #####

	class Discover(restful.Resource):
	    def get(self):
	    	lim = request.args.get('limit', 5000)
	    	movies = Movies.query.filter(Movies.poster != None).filter(Movies.year <= 2015).order_by(Movies.year.desc()).limit(lim).all()
	    	result = movie_schema.dump(movies)
	        return jsonify({"movies":result.data})

	api.add_resource(Discover, '/v1/discover','/v1/discover.json')

	class Wishlist(restful.Resource):
		def get(self):
			return jsonify({'whishlist':''})

		def post(self):
			args = parser.parse_args()
			return jsonify({'error':'none'})

		def delete(self):
			return jsonify({'error':False, 'message':'wishlist item'})

	api.add_resource(Wishlist, '/v1/wishlist','/v1/wishlist.json')

	
	class RegisterDevice(restful.Resource):
		def post(self):
			device_token = request.json.get('device_token')
			user = Users(device_token)
			db.session.add(user)
			db.session.commit()
			return jsonify({'user_id':user.id})
			

	api.add_resource(RegisterDevice, '/v1/registerdevice','/v1/registerdevice.json')
	

	if __name__ == '__main__':
	    app.run()
