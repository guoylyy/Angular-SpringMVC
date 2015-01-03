from app import app, db
from app.models import pushs
from flask import abort, jsonify, request
import jpush as jpush
import datetime
import json

@app.route('/news/pushs', methods = ['GET'])
def get_all_pushs():
    entities = pushs.Pushs.query.order_by(pushs.Pushs.id.desc()).all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/pushs/<int:id>', methods = ['GET'])
def get_pushs(id):
    entity = pushs.Pushs.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/pushs', methods = ['POST'])
def create_pushs():
    _jpush = jpush.JPush(app.config['PUSH_KEY'],app.config['PUSH_SECRET'])
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert=request.json['content'])
    push.platform = jpush.all_
    try:
        push.send()
        entity = pushs.Pushs(
            content = request.json['content']
        )
        entity.created_time = datetime.datetime.now()
        entity.success = True
        db.session.add(entity)
        db.session.commit()
        return jsonify(entity.to_dict()), 201
    except Exception, e:
        return jsonify(dict(result='fail')), 201
    

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
