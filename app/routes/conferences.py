from app import app, db
from app.models import conference
from flask import abort, jsonify, request
from app.extensions import files
import datetime
import json

@app.route('/news/conferences/<int:id>/file_upload/<string:ftype>', methods=['POST'])
def upload_file(id, ftype):
    entity = conference.Conference.query.get(id)
    if entity is None:
        abort(404)
    if ftype in conference.ConferenceAttachmentTypeEnum:
        filename = files.save(request.files['file'])
        c = conference.ConferenceFile(conference_id=entity.id,
                file_name=filename,file_path=files.url(filename),
                file_type=ftype)
        db.session.add(c)
        db.session.commit()
        return jsonify(dict(result='success'))
    else:
        abort(500)

@app.route('/news/conferences/dict', methods=['GET'])
def get_dict():
    return json.dumps([dict(data=d) for d in conference.ConferenceAttachmentTypeEnum],ensure_ascii=False)

@app.route('/news/conferences/<int:id>/get_file/<string:ftype>')
def get_file(id,ftype):
    if ftype in conference.ConferenceAttachmentTypeEnum:
        l = conference.ConferenceFile.query.filter(
                conference.ConferenceFile.conference_id==id,
                conference.ConferenceFile.file_type==ftype)
        return json.dumps([e.to_dict() for e in l],ensure_ascii=False)
    else:
        abort(500)

@app.route('/news/conferences', methods = ['GET'])
def get_all_conferences():
    entities = conference.Conference.query.all()
    return json.dumps([entity.to_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/conferences/content', methods = ['GET'])
def get_conference():
    entity = conference.Conference.query.first()
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/conferences/simple_content', methods = ['GET'])
def get_simple_conference():
    entity = conference.Conference.query.first()
    if not entity:
        abort(404)
    return jsonify(entity.to_simple_dict())


@app.route('/news/conferences', methods = ['POST'])
def create_conference():
    """
        TODO: update item names
    """
    entity = conference.Conference(
        intro_content = request.json['intro_content']
        , logistics_content = request.json['logistics_content']
        , layout_content = request.json['logistics_content']
        , agenda_content = request.json['logistics_content']
        , group_content = request.json['logistics_content']
        , title = request.json['title']
        , created_time = datetime.datetime.strptime(request.json['created_time'], "%Y-%m-%d").date()
        , updated_time = datetime.datetime.strptime(request.json['updated_time'], "%Y-%m-%d").date()
        , started_time = datetime.datetime.strptime(request.json['updated_time'], "%Y-%m-%d").date()
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
