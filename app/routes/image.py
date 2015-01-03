#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import image
from flask import abort, jsonify, request, send_file
from app.extensions import fs_store, files
import datetime
import json

@app.route('/news/mockimage', methods= ['GET'])
def mockimage():
	"""获取app导入页面图片"""
	entity = image.MockImage.query.first()
	return jsonify(entity.to_dict());

@app.route('/news/mockimage', methods=['POST'])
def update_mockimage():
	"""修改 app 开启页面"""
	try:
		filename = files.save(request.files['file'])
		filepath = files.url(filename)
		mockimages = image.MockImage.query.all()
		if len(mockimages) > 0:
			image.MockImage.query.delete()
		entity = image.MockImage(url=filepath)
		db.session.add(entity)
		db.session.commit()
		return jsonify(dict(result='success'))
	except Exception, e:
		raise e
		return jsonify(dict(result='fail'))


@app.route('/news/mainpage_images', methods=['GET'])
def main_page_images():
	"""获取主页滚动的广告图片列表"""
	images = image.MainPageImage.query.all()
	return json.dumps([im.to_dict() for im in images],ensure_ascii=False)

@app.route('/news/update_mainpage_image/<int:id>', methods=['POST'])
def update_mainpage_image(id):
	"""添加主页广告图片"""
	try:
		filename = files.save(request.files['file'])
		filepath = files.url(filename)
		en = image.MainPageImage.query.get(id)
		if not en:
			abort(404)
		entity = image.MainPageImage(link=filepath,name=filename,order=0,news_id=en.news_id)
		entity.id = en.id
		db.session.merge(entity)
		db.session.commit()
		return jsonify(dict(result='success'))
	except Exception, e:
		raise e
		return jsonify(dict(result='error'))

@app.route('/news/update_news_link/<int:id>', methods=['POST'])
def update_image_news_link(id):
	try:
		news_id = request.json['news_id']
		en = image.MainPageImage.query.get(id)
		if not en:
			abort(404)
		en.news_id = news_id
		db.session.merge(en)
		db.session.commit()
		return jsonify(dict(result='success'))
	except Exception, e:
		raise e
		return jsonify(dict(result='fail'))
