from app import app, db
from app.models import news
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/news', methods = ['GET'])
def get_all_news():
    entities = news.News.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/news/<int:id>', methods = ['GET'])
def get_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/news', methods = ['POST'])
def create_news():
    entity = news.News(
        title = request.json['title']
        , content = request.json['content']
        , create_time = datetime.datetime.strptime(request.json['create_time'], "%Y-%m-%d").date()
        , update_time = datetime.datetime.strptime(request.json['update_time'], "%Y-%m-%d").date()
        , author = request.json['author']
        , view_count = request.json['view_count']
        , is_draft = request.json['is_draft']
        , publisher = request.json['publisher']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/news/<int:id>', methods = ['PUT'])
def update_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    entity = news.News(
        title = request.json['title'],
        content = request.json['content'],
        create_time = datetime.datetime.strptime(request.json['create_time'], "%Y-%m-%d").date(),
        update_time = datetime.datetime.strptime(request.json['update_time'], "%Y-%m-%d").date(),
        author = request.json['author'],
        view_count = request.json['view_count'],
        is_draft = request.json['is_draft'],
        publisher = request.json['publisher'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/news/<int:id>', methods = ['DELETE'])
def delete_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
