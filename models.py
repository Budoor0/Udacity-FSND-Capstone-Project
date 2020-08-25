#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import os
from sqlalchemy import Column, String, Integer, create_engine
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from sqlalchemy.orm import backref
import psycopg2
import json


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


database_name = "capstone"
database_path = "postgres://{}:{}@{}/{}".format(
    'postgres', '123', 'localhost:5432', database_name)


db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
CREATE MODELS 
MOVIES, ACTORS, POSTER
'''

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_data = Column(String, nullable=False)
    actors = db.relationship('Actor', secondary='poster',
                             backref='movie', lazy=True)

    def __init__(self, title, release_data):
        self.title = title
        self.release_data = release_data

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_data': self.release_data,
            'actors': [actor.name for actor in self.actors]
        }


class Actor(db.Model):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(String)
    gendar = Column(String)
    movies = db.relationship('Movie', secondary='poster',
                             backref='actor', lazy=True)

    def __init__(self, name, age, gendar):
        self.name = name
        self.age = age
        self.gendar = gendar

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gendar': self.gendar,
            'movies': [movie.title for movie in self.movies]
        }


class Poster(db.Model):
    __tablename__ = 'poster'

    poster_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, db.ForeignKey(
        'movie.id', ondelete='CASCADE'), primary_key=True)
    actor_id = Column(Integer, db.ForeignKey(
        'actor.id', ondelete='CASCADE'), primary_key=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
