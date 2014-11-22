from app import app, db
from app.models import message
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/messages', methods = ['GET'])
def get_all_messages():
    entities = message.Message.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/messages/<int:id>', methods = ['GET'])
def get_message(id):
    entity = message.Message.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/messages', methods = ['POST'])
def create_message():
    entity = message.Message(
        content = request.json['content']
        , created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date()
        , publisher = request.json['publisher']
        , is_active = request.json['is_active']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/messages/<int:id>', methods = ['PUT'])
def update_message(id):
    entity = message.Message.query.get(id)
    if not entity:
        abort(404)
    entity = message.Message(
        content = request.json['content'],
        created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date(),
        publisher = request.json['publisher'],
        is_active = request.json['is_active'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/messages/<int:id>', methods = ['DELETE'])
def delete_message(id):
    entity = message.Message.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
