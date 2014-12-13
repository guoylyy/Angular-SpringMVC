import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_DATABASE_URI = 'mysql://root:a842637@127.0.0.1/news'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_ECHO = False
UPLOADED_FILES_DEST = os.path.join(basedir, 'app/dynamic/files')
UPLOADS_DEFAULT_URL = 'http://localhost:5001'