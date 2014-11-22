from app import app, db
from app.models import user
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/users', methods = ['GET'])
def get_all_users():
    entities = user.User.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/users/<int:id>', methods = ['GET'])
def get_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/users', methods = ['POST'])
def create_user():
    entity = user.User(
        account = request.json['account']
        , password = request.json['password']
        , name = request.json['name']
        , role = request.json['role']
        , email = request.json['email']
        , registered_time = datetime.datetime.strptime(request.json['registered_time'], "%Y-%m-%d").date()
        , is_active = request.json['is_active']
        , phone_number = request.json['phone_number']
        , description = request.json['description']
        , lastlogin_time = datetime.datetime.strptime(request.json['lastlogin_time'], "%Y-%m-%d").date()
        , myattr = request.json['myattr']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/users/<int:id>', methods = ['PUT'])
def update_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    entity = user.User(
        account = request.json['account'],
        password = request.json['password'],
        name = request.json['name'],
        role = request.json['role'],
        email = request.json['email'],
        registered_time = datetime.datetime.strptime(request.json['registered_time'], "%Y-%m-%d").date(),
        is_active = request.json['is_active'],
        phone_number = request.json['phone_number'],
        description = request.json['description'],
        lastlogin_time = datetime.datetime.strptime(request.json['lastlogin_time'], "%Y-%m-%d").date(),
        myattr = request.json['myattr'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
