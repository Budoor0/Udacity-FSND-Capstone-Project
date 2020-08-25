import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy


from app import create_app
from models import setup_db, Movie, Actor, Poster

from functools import wraps


capstone_casting_assistant = str(
    'Bearer ' + os.environ['capstone_casting_assistant'])
capstone_casting_director = str(
    'Bearer ' + os.environ['capstone_casting_director'])
capstone_executive_producer = str(
    'Bearer ' + os.environ['capstone_executive_producer'])


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', '123', 'localhost:5432', self.database_name)

        self.casting_assistant = {
            'Content-Type': 'application/json', 'Authorization': capstone_casting_assistant}
        self.casting_director = {
            'Content-Type': 'application/json', 'Authorization': capstone_casting_director}
        self.executive_producer = {
            'Content-Type': 'application/json', 'Authorization': capstone_executive_producer}

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

        # TEST INDEX ENDPOINT

    def test_index(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
# TEST GET ALL ACTORS error behavior
    def test1_404_if_actors_does_not_exist(self):

        res = self.client().get('/actors', headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

        # TEST GET ALL ACTORS success
    def test_get_actors(self):
        actor = Actor(name='Sarah', age=10, gendar='female')
        actor.insert()
        res = self.client().get('/actors', headers=self.casting_assistant)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # TEST GET ALL ACTORS without authorization
    def test_get_actors_without_authorization(self):
        actor = Actor(name='Sarah', age=10, gendar='female')
        actor.insert()
        res = self.client().get('/actors')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

        # TEST add  ACTOR success
    def test_add_actor(self):
        res = self.client().post('/actors',
                                 json={'name': 'EDIT name', 'age': 10, 'gendar': 'female'}, headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # TEST add  ACTOR error behavior
    def test_empty_post(self):
        res = self.client().post('/actors', json={}, headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

        # TEST add  ACTOR casting assistant
    def test_403_add_actor_casting_assistant(self):
        res = self.client().post('/actors',
                                 json={'name': 'EDIT name', 'age': 10, 'gendar': 'female'}, headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

        # TEST PATCH ACTORS success

    def test_update_actor(self):
        actor = Actor(name='Maha', age=50, gendar='Female')
        actor.insert()
        actorId = actor.id
        res = self.client().patch(f'/actors/{actor.id}', json={
            'name': 'EDIT name', 'age': 10, 'gendar': 'female'}, headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

       # TEST PATCH ACTORS error behavior
    def test_400_update_actor(self):
        actor = Actor(name='Maha', age=50, gendar='Female')
        actor.insert()
        actorId = actor.id
        res = self.client().patch(
            f'/actors/{actor.id}', headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

        # TEST PATCH ACTORS casting assistant
    def test_403_update_actor_casting_assistant(self):
        actor = Actor(name='Maha', age=50, gendar='Female')
        actor.insert()
        actorId = actor.id
        res = self.client().patch(f'/actors/{actor.id}', json={
            'name': 'EDIT name', 'age': 10, 'gendar': 'female'}, headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    # test DELETE  ACTORS success
    def test_delete_actor(self):
        actor = Actor(name='Maha', age=10, gendar='Female')
        actor.insert()
        actorId = actor.id
        res = self.client().delete(
            f'/actors/{actor.id}', headers=self.executive_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    # test DELETE  ACTORS error behavior

    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.executive_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # test DELETE  ACTORS casting assistant
    def test_403_delete_actor_casting_assistant(self):
        actor = Actor(name='Maha', age=10, gendar='Female')
        actor.insert()
        actorId = actor.id
        res = self.client().delete(
            f'/actors/{actor.id}', headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#------------------------------------------------------------#
#------------------------------------------------------------#

        # TEST GET ALL MOVIESE error behavior

    def test1_404_if_movies_does_not_exist(self):

        res = self.client().get('/movies', headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # TEST GET ALL MOVIES success
    def test_get_movies(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        res = self.client().get('/movies', headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # TEST GET ALL MOVIES without authorization
    def test_get_movies_without_authorization(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        res = self.client().get('/movies')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        # TEST add  MOVIES success

    def test_add_movies(self):
        res = self.client().post('/movies',
                                 json={'title': 'test update movies one', 'release_data': '5/4/2020'}, headers=self.executive_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # TEST add  MOVIES error behavior
    def test_empty_post_movies(self):
        res = self.client().post('/movies', json={}, headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

        # TEST add  MOVIES casting assistant
    def test_403_add_movies_casting_assistant(self):
        res = self.client().post('/movies',
                                 json={'title': 'test update movies one', 'release_data': '5/4/2020'}, headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

        # TEST add  MOVIES casting director
    def test_403_add_movies_casting_director(self):
        res = self.client().post('/movies',
                                 json={'title': 'test update movies one', 'release_data': '5/4/2020'}, headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

# TEST PATCH MOVIES success
    def test_update_movie(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().patch(f'/movies/{movie.id}', json={
            'title': 'test update movies one', 'release_data': '5/4/2020'}, headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

       # TEST PATCH MOVIES error behavior
    def test_400_update_movie(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().patch(
            f'/movies/{movie.id}', headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    # TEST PATCH MOVIES casting assistant
    def test_403_update_movie_casting_assistant(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().patch(f'/movies/{movie.id}', json={
            'title': 'test update movies one', 'release_data': '5/4/2020'}, headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

  # test DELETE  MOVIES success
    def test_delete_movie(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().delete(
            f'/movies/{movie.id}', headers=self.executive_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    # test DELETE  MOVIES error behavior

    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.executive_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

  # test DELETE  MOVIES casting_director
    def test_403_delete_movie_casting_director(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().delete(
            f'/movies/{movie.id}', headers=self.casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

  # test DELETE  MOVIES success
    def test_403_delete_movie_casting_assistant(self):
        movie = Movie(title='test movies one', release_data='5/4/2020')
        movie.insert()
        movieId = movie.id
        res = self.client().delete(
            f'/movies/{movie.id}', headers=self.casting_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
