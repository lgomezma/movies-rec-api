from flask import Flask, jsonify
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

		def __init__(self, id, title):
			self.id = id
			self.title = title

	##### SCHEMAS #####

	class MovieSchema(ma.Schema):
	    class Meta:
	        # Fields to expose
	        fields = ('id', 'title')

	movie_schema = MovieSchema(many=True)

	##### API #####

	class HelloWorld(restful.Resource):
	    def get(self):
	    	movies = Movies.query.limit(5000).all()
	    	result = movie_schema.dump(movies)
	        return jsonify({"movies":result.data})

	api.add_resource(HelloWorld, '/')

	if __name__ == '__main__':
	    app.run(debug=True)
