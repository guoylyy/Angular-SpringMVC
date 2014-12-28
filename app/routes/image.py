#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import app, db
from app.models import image
from flask import abort, jsonify, request, send_file
from app.extensions import fs_store, files
import datetime
import json

@app.route('/news/mockimage')
def mockimage():
	"""获取app导入页面图片"""
	filename = "static/image/mockimage.jpg"
	return send_file(filename,mimetype='image/jpeg')

@app.route('/news/mockimage/update')
def update_mockimage():
	return 'This api is not available now.'

@app.route('/news/mainpage_images', methods=['GET'])
def main_page_images():
	"""获取主页滚动的广告图片列表"""
	images = image.MainPageImage.query.all()
	return json.dumps([im.to_dict() for im in images],ensure_ascii=False)

@app.route('/news/add_mainpage_image', methods=['POST'])
def add_mainpage_image():
	"""添加主页广告图片"""
	try:
		filename = files.save(request.files['file'])
		filepath = files.url(filename)
		entity = image.MainPageImage(link=filepath,name=filename,order=0,news_id=1)
		db.session.add(entity)
		db.session.commit()
		return jsonify(dict(result='success'))
	except Exception, e:
		raise e
		return jsonify(dict(result='error'))
