from sqlalchemy.orm.exc import NoResultFound
from app import db

def find_or_create_thumbnail(obj, imageset, width=None, height=None):
	assert width is not None or height is not None 
	try:
		image = imageset.find_thumbnail(width=width, height=height)
	except NoResultFound:
		imageset.generate_thumbnail(width=width, height=height) 
		db.session.add(obj)
		db.session.commit()
		image = imageset.find_thumbnail(width=width, height=height)
	return image