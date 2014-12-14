from app import app, db
from app.models import image
from flask import abort, jsonify, request, send_file
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

@app.route('/news/main_page_images', methods=['GET'])
def main_page_images_url():
	"""
		TODO: Add internal link of post: post_id
	"""
	l = []
	for i in range(5):
		l.add(dict(id=i))
	return json.dumps(l)

@app.route('/news/main_page_image/<int:id>',methods=['GET'])
def main_page_image(id):
	filename = "files/mainpage/m" + str(id)+".jpg"
	return send_file(filename,mimetype='image/jpeg')
