#!flask/bin/python
from migrate.versioning import api
from test_config import SQLALCHEMY_DATABASE_URI
from test_config import SQLALCHEMY_MIGRATE_REPO
from flask.ext.sqlalchemy import SQLAlchemy
from app import create_test_app
import os.path

app = create_test_app()
db = SQLAlchemy(app)
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
