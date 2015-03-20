from app import app, db
from app.models import inform
from flask import abort, jsonify, request
import datetime
import json

@app.route('/news/system_time', methods = ['GET'])
def get_system_time():
    return jsonify({'system_time':datetime.datetime.now().isoformat()})

@app.route('/news/informs', methods = ['GET'])
@app.route('/news/placard/all', methods=['GET'])
def get_all_informs():
    entities = inform.Inform.query.order_by(inform.Inform.create_time.desc()).limit(3)
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/news/informs/<int:id>', methods = ['GET'])
def get_inform(id):
    entity = inform.Inform.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/informs', methods = ['POST'])
def create_inform():
    entity = inform.Inform(
        title = request.json['title']
    )
    entity.create_time = datetime.datetime.now()
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/informs/<int:id>', methods = ['PUT'])
def update_inform(id):
    entity = inform.Inform.query.get(id)
    if not entity:
        abort(404)
    entity.title = request.json['title']
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/news/informs/<int:id>', methods = ['DELETE'])
def delete_inform(id):
    entity = inform.Inform.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
