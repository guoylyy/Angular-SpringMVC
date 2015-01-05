from app import app, db
from app.models import movie
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/movies', methods = ['GET'])
def get_all_movies():
    entities = movie.Movie.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/movies/<int:id>', methods = ['GET'])
def get_movie(id):
    entity = movie.Movie.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/movies', methods = ['POST'])
def create_movie():
    entity = movie.Movie(
        name = request.json['name']
        , url = request.json['url']
        , size = request.json['size']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/movies/<int:id>', methods = ['PUT'])
def update_movie(id):
    entity = movie.Movie.query.get(id)
    if not entity:
        abort(404)
    entity = movie.Movie(
        name = request.json['name'],
        url = request.json['url'],
        size = request.json['size'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/movies/<int:id>', methods = ['DELETE'])
def delete_movie(id):
    entity = movie.Movie.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
