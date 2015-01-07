#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import conference
from app.tools import _rename_file
from flask import abort, jsonify, request
from app.extensions import files
from werkzeug.utils import secure_filename
import datetime
import json

@app.route('/news/conferences/<int:id>/file_upload/<string:ftype>', methods=['POST'])
def upload_file(id, ftype):
    "upload file for conferences"
    entity = conference.Conference.query.get(id)
    if entity is None:
        abort(404)
    if ftype in conference.ConferenceAttachmentTypeEnum:
        realname = request.files['file'].filename.encode('utf-8')
        o_file = request.files['file']
        o_file.filename = _rename_file(o_file.filename) 
        filename = files.save(o_file)
        c = conference.ConferenceFile(conference_id=entity.id,
                file_name=realname,file_path=files.url(filename),
                file_type=ftype)
        db.session.add(c)
        db.session.commit()
        return jsonify(dict(result='success'))
    else:
        abort(500)

@app.route('/news/conferences/file/<int:id>', methods=['POST'])
def delete_uploaded_file(id):
    "删除上传的文件"
    entity = conference.ConferenceFile.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204

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
    "获取会议列表(暂时废弃不用)"
    entities = conference.Conference.query.all()
    return json.dumps([entity.to_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/conferences/content', methods = ['GET'])
def get_conference():
    "获取会议所有详情"
    entity = conference.Conference.query.first()
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/news/conferences/simple_content', methods = ['GET'])
def get_simple_conference():
    "获取会议的简介(不带详情版本)"
    entity = conference.Conference.query.first()
    if not entity:
        abort(404)
    return jsonify(entity.to_simple_dict())

@app.route('/news/conferences/<int:id>', methods = ['GET'])
def get_conference_by_id(id):
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    return json.dumps(entity.to_dict(),ensure_ascii=False)

@app.route('/news/conferences', methods = ['POST'])
def create_conference():
    """
        添加一个会议，目前暂时只做测试的时候用
        添加会议中每一个 content 都是 html 内容
    """
    entity = conference.Conference(
         intro_content = request.json['intro_content']
        , logistics_content = request.json['logistics_content']
        , layout_content = request.json['layout_content']
        , agenda_content = request.json['agenda_content']
        , group_content = request.json['group_content']
        , title = request.json['title']
        , started_time = datetime.datetime.strptime(request.json['started_time'], "%Y-%m-%d %H:%M:%S")
        , is_draft = request.json['is_draft']
    )
    entity.created_time = datetime.datetime.now()
    entity.updated_time = datetime.datetime.now()
    entity.view_count = 0
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/news/conferences/<int:id>', methods = ['PUT'])
def update_conference(id):
    "更新会议接口，需要修改支持更高级的功能"
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    entity = conference.Conference(
        intro_content = request.json['intro_content']
        , logistics_content = request.json['logistics_content']
        , layout_content = request.json['layout_content']
        , agenda_content = request.json['agenda_content']
        , group_content = request.json['group_content'],
        title = request.json['title'],
        started_time = datetime.datetime.strptime(request.json['started_time'], "%Y-%m-%d %H:%M:%S"),
        is_draft = request.json['is_draft'],
        id = id
    )
    entity.updated_time = datetime.datetime.now()
    db.session.merge(entity)
    db.session.commit()
    entity = conference.Conference.query.get(id)
    return jsonify(entity.to_dict()), 200

@app.route('/news/conferences/<int:id>', methods = ['DELETE'])
def delete_conference(id):
    "删除一个会议实体，目前来说不开放这个功能"
    entity = conference.Conference.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
