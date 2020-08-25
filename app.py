import os
import json
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import sys
from sqlalchemy.orm import backref

from models import setup_db, db, Movie, Actor, Poster
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    setup_db(app)

    # CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        return f'Hello, Finall project ! '

    # get all actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def show_actors(payload):
        actors = Actor.query.all()
        if not actors:
            abort(404)
        formatActors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'Actors': formatActors
        })

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def show_actors_info(payload, actor_id):

        try:
            actors = Actor.query.get(actor_id)
            if actors is None:
                abort(404)

            formatActors = [actors.format()]

            return jsonify({
                'success': True,
                'Actors': formatActors
            }), 200

        except:
            abort(400)

    # get all movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def show_movies(payload):

        movies = Movie.query.all()
        if not movies:
            abort(404)
        formatMovies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': formatMovies
        })

    # get movie information
    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def show_movies_info(payload, movie_id):

        try:
            movies = Movie.query.get(movie_id)
            if movies is None:
                abort(404)

            formatMovies = [movies.format()]

            return jsonify({
                'success': True,
                'movies': formatMovies
            }), 200

        except:
            abort(400)

    # add new actors
    @app.route('/actors', methods=['POST'])
    @requires_auth(permission='post:actors')
    def add_new_actors(payload):
        body = request.get_json()

        actor_name = body.get('name', None)
        actor_age = body.get('age', None)
        actor_gendar = body.get('gendar', None)

        if not (actor_name and actor_age and actor_gendar):
            abort(400)

        try:

            new_actor = Actor(name=actor_name, age=actor_age,
                              gendar=actor_gendar)
            new_actor.insert()

            format_actor = new_actor.format()

            return jsonify({
                'success': True,
                'actor': format_actor
            }), 200

        except:
            abort(422)

    # add new movies
    @app.route('/movies', methods=['POST'])
    @requires_auth(permission='post:movies')
    def add_new_movies(payload):
        body = request.get_json()

        movie_title = body.get('title', None)
        movie_release_data = body.get('release_data', None)

        if not (movie_title and movie_release_data):
            abort(400)

        try:

            new_movie = Movie(title=movie_title,
                              release_data=movie_release_data)
            new_movie.insert()

            format_movie = new_movie.format()

            return jsonify({
                'success': True,
                'movie': format_movie
            }), 200

        except:
            abort(422)

    # edit actors information
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth(permission='patch:actors')
    def edit_actor(payload, actor_id):

        body = request.get_json()
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            if 'name' in body:
                actor.name = body.get('name', None)

            if 'age' in body:
                actor.age = body.get('age', None)

            if 'gendar' in body:
                actor.gendar = body.get('gendar', None)

            actor.update()
            format_actor = [actor.format()]

            return jsonify({
                'success': True,
                'actor': format_actor
            }), 200

        except:
            abort(400)

    # edit movies information
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth(permission='patch:movies')
    def edit_movie(payload, movie_id):

        body = request.get_json()
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            if 'title' in body:
                movie.title = body.get('title', None)

            if 'release_data' in body:
                movie.release_data = body.get('release_data', None)

            movie.update()
            format_movie = [movie.format()]

            return jsonify({
                'success': True,
                'movie': format_movie
            }), 200

        except Exception as error:
            raise error

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth(permission='delete:actors')
    def delete_actor_by_id(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'delete': actor_id
            }), 200

        except:
            abort(422)

    # delete movie
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth(permission='delete:movies')
    def delete_movie_by_id(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200

        except:
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(403)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "permission not allowed"
        }), 403

    @app.errorhandler(AuthError)
    def authError_handler(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
