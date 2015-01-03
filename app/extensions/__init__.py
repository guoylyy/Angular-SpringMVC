import os
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_imageattach.stores.fs import FileSystemStore
from flask.ext.uploads import UploadSet, ALL, configure_uploads

basedir = os.path.abspath(os.path.dirname(__file__))
IMAGE_UPLOAD_URL = os.path.join(basedir, 'userimages')
IMAGE_URL = 'file:///Users/globit/git/news_api/app/extensions/userimages/'

fs_store = FileSystemStore(IMAGE_UPLOAD_URL, IMAGE_URL)
files = UploadSet('files', ALL)
configure_uploads(app,(files,))
