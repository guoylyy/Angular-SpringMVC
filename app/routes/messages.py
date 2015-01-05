#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import message, user
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/placard/all', methods=['GET'])
def get_placard():
    """获取公告 TODO:添加和删除公告，我擦啦"""
    return json.dumps([entity.to_dict() for entity in message.Placard.query.all()],ensure_ascii=False)

@app.route('/news/message/send', methods = ['POST'])
def send_message():
    """用户添加message"""
    token = request.json['token']
    u = user.User.query.filter(user.User.token == token).first()
    if not u:
        abort(404)
    m = message.Message(
        content = request.json['content'],
        created_time = datetime.datetime.now(),
        user_id = u.id,
        publisher = u.name)
    db.session.add(m)
    db.session.commit()
    return jsonify(m.to_dict()), 201

@app.route('/news/messages', methods = ['GET'])
def get_all_messages():
    """
        按照时间序列获取前 100 条 message
        @limit:100
    """
    entities = message.Message.query.order_by(message.Message.created_time.desc()).limit(100)
    return json.dumps([entity.to_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/messages/<int:id>', methods = ['GET'])
def get_message(id):
    entity = message.Message.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/messages', methods = ['POST'])
def admin_create():
    entity = message.Message(
        content = request.json['content'],
        is_active = True
        )
    entity.created_time = datetime.datetime.now()
    entity.publisher = '管理员'
    u = user.User.query.filter(user.User.role == 'admin').first()
    if not u:
        abort(404)
    entity.user_id = u.id
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
        created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d %H:%M:%S"),
        is_active = request.json['is_active'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    entity = message.Message.query.get(id)
    return jsonify(entity.to_dict()), 200

@app.route('/news/messages/<int:id>', methods = ['DELETE'])
def delete_message(id):
    entity = message.Message.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
