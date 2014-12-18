from app import app, db
from app.models import image
from flask import abort, jsonify, request, send_file
from app.extensions import fs_store, files
import datetime
import json

@app.route('/news/mockimage')
def mockimage():
	"""
		To get the image of mock 
	"""
	filename = "static/image/mockimage.jpg"
	return send_file(filename,mimetype='image/jpeg')

@app.route('/news/mockimage/update')
def update_mockimage():
	return 'This api is not available now.'

@app.route('/news/mainpage_images', methods=['GET'])
def main_page_images():
	"""
		TODO: Add internal link of post: post_id
	"""
	images = image.MainPageImage.query.all()
	return json.dumps([im.to_dict() for im in images],ensure_ascii=False)


@app.route('/news/add_mainpage_image', methods=['POST'])
def add_mainpage_image():
	"""
	"""
	try:
		filename = files.save(request.files['file'])
		filepath = files.url(filename)
		entity = image.MainPageImage(link=filepath,name=filename,order=0)
		db.session.add(entity)
		db.session.commit()
		return jsonify(dict(result='success'))
	except Exception, e:
		raise e
		return jsonify(dict(result='error'))
