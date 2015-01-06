#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import news
from flask import abort, jsonify, request
from sqlalchemy_imageattach.entity import Image, image_attachment, store_context
from app.extensions import fs_store, files
from requests import get
import datetime
import json

@app.route('/news/news/<int:id>/upload_pdf',methods=['POST'])
def upload_pdf(id):
    try:
        filename = files.save(request.files['file'])
        entity = news.NewsFile(news_id=id,filename=filename, filepath=files.url(filename))
        db.session.add(entity)
        db.session.commit()
        return jsonify(dict(result='success'))
    except Exception, e:
        raise e
        return jsonify(dict(result='error'))
    
@app.route('/news/news_attchments/<int:id>',methods=['GET'])
def get_attachments(id):
    entity = news.News.query.get(id)
    if entity is None:
        abort(404)
    return json.dumps(entity.get_files(),ensure_ascii=False)


@app.route('/news/topic/add', methods = ['POST'])
def add_topic():
    entity = news.Topic(
        title = request.json['title']
        )
    db.session.add(entity)
    db.session.commit()
    image = get('http://ww3.sinaimg.cn/mw690/63ea4d33gw1ejhpwui71sj20u00k045s.jpg').content
    with store_context(fs_store):
        t_image = news.TopicImage(
            topic_id=entity.id
            )
        t_image.image.from_blob(image)
        db.session.add(t_image)
        db.session.commit()
    return jsonify(entity.to_dict())

@app.route('/news/topic/<int:id>')
def get_topic(id):
    entity = news.Topic.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.list())

@app.route('/news/topic/<int:id>/add_news/<int:nid>', methods = ['GET'])
def add_topic_news(id,nid):
    topic = news.Topic.query.get(id)
    news = news.News.query.get(nid)
    if topic is None or news is None:
        abort(404)
    topic.newss.add(news)
    db.session.add(topic)
    db.session.commit()
    return jsonify(dict(result='success'))

@app.route('/news/topic/<int:id>/upload_image',methods = ['POST'])
def add_topic_image(id):
    image = get('http://ww3.sinaimg.cn/mw690/63ea4d33gw1ejhpwui71sj20u00k045s.jpg').content
    with store_context(fs_store):
        t_image = news.TopicImage(
            topic_id=entity.id
            )
        t_image.image.from_blob(image)
        db.session.add(t_image)
        db.session.commit()
    return jsonify(dict(result='success'))

@app.route('/news/topics', methods = ['GET'])
def get_all_topics():
    topics = news.Topic.query.all()
    return json.dumps([entity.to_dict() for entity in topics],ensure_ascii=False)

@app.route('/news/simple_news', methods = ['GET'])
def get_simple_news():
    """ 获取所有新闻的预览列表 """
    entities = news.News.query.order_by(news.News.update_time.desc()).all()
    return json.dumps([entity.to_list_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/news', methods = ['GET'])
def get_all_news():
    entities = news.News.query.order_by(news.News.update_time.desc()).all()
    return json.dumps([entity.to_dict() for entity in entities],ensure_ascii=False)

@app.route('/news/news/<int:id>', methods = ['GET'])
def get_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    return json.dumps(entity.to_dict(),ensure_ascii=False)

@app.route('/news/news', methods = ['POST'])
def create_news():
    entity = news.News(
        title = request.json['title']
        , content = request.json['content']
    )
    entity.is_draft = False
    entity.update_time = datetime.datetime.now()
    entity.create_time = datetime.datetime.now()
    entity.author = '管理员'
    entity.view_count = 0
    if(len(request.json['video_link']) is not None):
        entity.has_video = True
        entity.video_link = request.json['video_link']
    else:
        entity.has_video = False
    try:
        with store_context(fs_store):
            if(request.json['temp_image'] is not None):
                with open(files.path(request.json['temp_image'])) as f:
                    entity.icon.from_file(f)
                    db.session.add(entity)
                    db.session.commit()
                    return jsonify(entity.to_dict()), 201
            else:
                abort(500)
    except Exception, e:
        raise e
        abort(500)


@app.route('/news/news/<int:id>', methods = ['PUT'])
def update_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    entity.title = request.json['title']
    entity.content = request.json['content']
    if(request.json['video_link'] is not None and len(request.json['video_link']) > 0):
        entity.has_video = True
        entity.video_link = request.json['video_link']
    else:
        entity.has_video = False
        entity.video_link = None
    
    try:
        with store_context(fs_store):
            if('temp_image' in request.json.keys() and request.json['temp_image'] is not None):
                with open(files.path(request.json['temp_image'])) as f:
                    entity.icon.from_file(f)
                    db.session.merge(entity)
                    db.session.commit()
            else:
                db.session.merge(entity)
                db.session.commit()
            return jsonify(entity.to_dict()), 200
    except Exception, e:
        raise e
        abort(500)


@app.route('/news/news/<int:id>', methods = ['DELETE'])
def delete_news(id):
    entity = news.News.query.get(id)
    if not entity:
        abort(404)
    with store_context(fs_store):
        db.session.delete(entity)
        db.session.commit()
        return '', 204
