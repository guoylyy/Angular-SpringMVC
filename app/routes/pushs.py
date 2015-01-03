from app import app, db
from app.models import pushs
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/pushs', methods = ['GET'])
def get_all_pushs():
    entities = pushs.Pushs.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/pushs/<int:id>', methods = ['GET'])
def get_pushs(id):
    entity = pushs.Pushs.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/pushs', methods = ['POST'])
def create_pushs():
    entity = pushs.Pushs(
        content = request.json['content']
        , created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date()
        , success = request.json['success']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/pushs/<int:id>', methods = ['PUT'])
def update_pushs(id):
    entity = pushs.Pushs.query.get(id)
    if not entity:
        abort(404)
    entity = pushs.Pushs(
        content = request.json['content'],
        created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date(),
        success = request.json['success'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/pushs/<int:id>', methods = ['DELETE'])
def delete_pushs(id):
    entity = pushs.Pushs.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
