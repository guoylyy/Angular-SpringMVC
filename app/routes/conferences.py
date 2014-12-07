from app import app, db
from app.models import conference
from flask import abort, jsonify, request
import datetime
import json



@app.route('/news/conferences', methods = ['GET'])
def get_all_conferences():
    entities = conference.Conference.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/conferences/<int:id>', methods = ['GET'])
def get_conference(id):
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/conferences', methods = ['POST'])
def create_conference():
    entity = conference.Conference(
        intro_content = request.json['intro_content']
        , logistics_content = request.json['logistics_content']
        , title = request.json['title']
        , created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date()
        , updated_time = datetime.datetime.strptime(request.json['updated_time'], "%Y-%m-%d").date()
        , view_count = request.json['view_count']
        , is_draft = request.json['is_draft']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/conferences/<int:id>', methods = ['PUT'])
def update_conference(id):
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    entity = conference.Conference(
        intro_content = request.json['intro_content'],
        logistics_content = request.json['logistics_content'],
        title = request.json['title'],
        created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date(),
        updated_time = datetime.datetime.strptime(request.json['updated_time'], "%Y-%m-%d").date(),
        view_count = request.json['view_count'],
        is_draft = request.json['is_draft'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/conferences/<int:id>', methods = ['DELETE'])
def delete_conference(id):
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
