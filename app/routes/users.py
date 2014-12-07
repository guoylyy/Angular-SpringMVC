from app import app, db
from app.models import user
from flask import abort, jsonify, request
from sqlalchemy_imageattach.entity import Image, image_attachment, store_context
from app.extensions import fs_store
from requests import get
import datetime
import json
import hashlib

@app.route('/news/login', methods= ['POST'])
def login():
    """
        Make the lifecycle of login procedure
    """
    entity = user.User(
          account = request.json['account']
        , password = request.json['password'])
    u = user.User.query.filter(user.User.account == entity.account).first()
    if not u:
        abort(404)
    if entity.password == u.password:
        if u.token is None:
            u.generate_token()
            db.session.merge(u)
            db.session.commit()
        return jsonify(u.to_dict())
    abort(500)

@app.route('/news/user/profile', methods = ['POST'])
def profile():
    """
        Get login user profile
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    return jsonify(u.to_dict())

@app.route('/news/user/<int:id>/update_name', methods = ['POST'])
def update_name(id):
    """
        Update user real name
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    if u.id is not id:
        abort(500)
    u.name = request.json['name']
    u.nickname = request.json['nickname']
    db.session.merge(u)
    db.session.commit()
    return jsonify(u.to_dict())

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
    header = get('http://ww3.sinaimg.cn/mw690/63ea4d33gw1ejhpwui71sj20u00k045s.jpg').content
    try:
        with store_context(fs_store):
            entity.generate_token()
            entity.header_icon.from_blob(header)
            db.session.add(entity)
            db.session.commit()
            return jsonify(entity.to_dict()), 201
    except Exception, e:
        abort(500)

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
    header = get('http://ww3.sinaimg.cn/mw690/63ea4d33gw1ejhpwui71sj20u00k045s.jpg').content
    with store_context(fs_store):
        entity.header_icon.from_blob(header)
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
