#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import user
from app.tools import _rename_file
from flask import abort, jsonify, request, send_file
from sqlalchemy_imageattach.entity import Image, image_attachment, store_context
from app.extensions import fs_store, files
from requests import get
import datetime
import json
import hashlib
import csv

@app.route('/news/users/user_list_csv', methods=['GET'])
def user_list_csv():
    """
        admin can generate a user csv which contains all user info
    """
    us = user.User.query.all()
    filename = 'xxx.csv'
    csv_name = _rename_file(filename)
    url =  app.config['CSV_FILES_DEST'] + '/' + csv_name
    with open(url, 'wb') as csvfile:
        #fieldnames = ['账号', '姓名', '描述', '角色', '邮箱', '电话', '工作电话', '公司', '部门', '职位']
        fieldnames = []
        if len(us) > 0:
            fieldnames = us[0].to_csv_dict().keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for u in us:
            dct = u.to_csv_dict()
            n_items = {}
            for name in fieldnames:
                if dct[name] is not None:
                    n_items[name] = dct[name].encode('utf-8')
                else:
                    n_items[name] = ''
            writer.writerow(n_items)
    return send_file(url)

@app.route('/news/admin_login', methods = ['POST'])
def admin_login():
    """
        Administrator login to backend
    """
    account = request.json['account']
    password = request.json['password']
    u = user.User.query.filter(user.User.account == account).first()
    if not u:
        abort(404)
    if u.password == password and u.role == 'admin':
        if u.token is None:
            u.generate_token()
            db.session.merge(u)
            db.session.commit()
        return jsonify(u.to_dict())
    else:
        abort(500)

@app.route('/news/register', methods= ['POST'])
def register():
    """
        User registeration
        #TODO duplicative code 
    """
    if user.User.query.filter(user.User.name == request.json['name']).count() > 0:
        abort(500)
    entity = user.User(
        account = request.json['account']
        , password = request.json['password']
        , name = request.json['name']
        , company = request.json['company']
        , phone_number = request.json['phone_number']
        , email = request.json['email']
        , title = request.json['title']
    )
    entity.registered_time = datetime.datetime.now().date();
    entity.lastlogin_time = datetime.datetime.now().date();
    entity.myattr = ''  #无用字段
    entity.is_active = True
    entity.is_vip = False
    entity.role = 'user'
    try:
        with store_context(fs_store):
            with open('app/static/image/default_header.png') as f:
                entity.generate_token()
                entity.header_icon.from_file(f)
                db.session.add(entity)
                db.session.commit()
                return jsonify(entity.to_dict()), 201
    except Exception, e:
        abort(500)

@app.route('/news/login', methods= ['POST'])
def login():
    """
        Make the lifecycle of login procedure
    """
    entity = user.User(
          account = request.json['account']
        , password = request.json['password'])
    u = user.User.query.filter(user.User.account == entity.account).first()
    if not u or not u.is_active:
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

@app.route('/news/user/update_header', methods = ['POST'])
def update_header():
    """
        Give a link of image, then update user header icon
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    try:
        with store_context(fs_store):
            with open(files.path(request.json['header'])) as f:
                u.header_icon.from_file(f)
                db.session.merge(u)
                db.session.commit()
        return jsonify(u.to_dict())
    except Exception, e:
        return jsonify(dict(result='fail',message='Can not find image error.'))
    

@app.route('/news/user/<int:id>/update_name', methods = ['POST'])
def update_name(id):
    """
        Update user real name
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    if u.id != id:
        print "user id is wrong." #TODO: Support log system
        abort(500)
    u.name = request.json['name']
    u.nickname = request.json['nickname']
    db.session.merge(u)
    db.session.commit()
    return jsonify(u.to_dict())

@app.route('/news/user/<int:id>/update_profile', methods = ['POST'])
def update_user_profile(id):
    """
        Update user real name
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    if u.id != id:
        print "user id is wrong." #TODO: Support log system
        abort(500)
    u.name = request.json['name']
    u.nickname = request.json['nickname']
    with store_context(fs_store):
        with open(files.path(request.json['header'])) as f:
            u.header_icon.from_file(f)
            db.session.merge(u)
            db.session.commit()
    db.session.merge(u)
    db.session.commit()
    return jsonify(u.to_dict())

@app.route('/news/user/<int:id>/update_user_profile', methods = ['POST'])
def update_user_profile_deep(id):
    """
        Update user real name
    """
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if u is None:
        abort(404)
    if u.id != id:
        print "user id is wrong." #TODO: Support log system
        abort(500)
    u.name = request.json['name']
    u.title = request.json['title']
    u.company = request.json['company']
    u.phone_number = request.json['phone_number']
    u.email = request.json['email']
    db.session.merge(u)
    db.session.commit()
    return jsonify(u.to_dict())


@app.route('/news/user/upload_icon', methods = ['POST'])
def upload_icon():
    """
        Update user's header icon
    """
    filename = files.save(request.files['file']) # get file and save as header icon
    return jsonify(dict(filename=filename))


@app.route('/news/users', methods = ['GET'])
def get_all_users():
    #entities = user.User.query.order_by(user.User.id.desc()).all()
    entities = user.User.query.order_by(user.User.id.desc()).filter(user.User.role != 'admin').filter(user.User.is_active==True)
    return json.dumps([entity.to_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/users/<int:id>', methods = ['GET'])
def get_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/users', methods = ['POST'])
def create_user():
    if user.User.query.filter(user.User.name == request.json['name']).count() > 0:
        abort(500)
    entity = user.User(
        account = request.json['account']
        , password = request.json['password']
        , name = request.json['name']
        , is_vip = request.json['is_vip']
        , nickname = request.json['nickname']
        , description = request.json['description']
    )
    entity.registered_time = datetime.datetime.now().date();
    entity.lastlogin_time = datetime.datetime.now().date();
    entity.myattr = ''
    entity.is_active = True
    entity.role = 'user'
    entity.company = ''
    #header = get('http://ww3.sinaimg.cn/mw690/63ea4d33gw1ejhpwui71sj20u00k045s.jpg').content
    try:
        with store_context(fs_store):
            with open('app/static/image/default_header.png') as f:
                entity.generate_token()
                entity.header_icon.from_file(f)
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
        name = request.json['name'],
        email = request.json['email'],
        phone_number = request.json['phone_number'],
        description = request.json['description'],
        nickname = request.json['nickname'],
        is_vip = request.json['is_vip'],
        id = id
    )

    if request.json['password'] !=  None and request.json['password'] != '':
        entity.password = request.json['password']
    with store_context(fs_store):
        db.session.merge(entity)
        db.session.commit()
        entity = user.User.query.get(id)
        return jsonify(entity.to_dict()), 200

@app.route('/news/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    with store_context(fs_store):
        entity.is_active = False
        db.session.merge(entity)
        db.session.commit()
        return '', 204
